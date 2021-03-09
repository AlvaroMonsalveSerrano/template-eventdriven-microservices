
import uuid
import logging

from flask import Flask, jsonify, request, current_app
from appams.domain import commands
from appams.views import views_cqrs
from appams import bootstrap

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

bus = bootstrap.bootstrap()


@app.route("/", methods=['GET'])
def root():
    """
    Root entrypoint

    Tot test: curl http://localhost:5000/

    :return: str
    """
    current_app.logger.info(f"[*] /root")
    return jsonify({'result': 'Ok'}), 200


@app.route("/liveness", methods=['GET'])
def liveness():
    """
    Liveness entrypoint.

    To test: curl http://localhost:5000/liveness

    :return: str
    """
    current_app.logger.info(f"[*] /liveness")

    command_liveness = commands.Liveness()

    response_use_case = bus.handle(message=command_liveness)

    if len(response_use_case) > 0:
        result_handler = response_use_case.pop(0)
    else:
        result_handler = "Empty"

    return result_handler, 200


@app.route("/rediness", methods=['GET'])
def rediness():
    """
    Rediness entrypoint.

    To test: curl http://localhost:5000/rediness

    :return: str
    """
    current_app.logger.info(f"[*] /rediness")

    command_rediness = commands.Rediness()

    response_use_case = bus.handle(message=command_rediness)

    if len(response_use_case) > 0:
        result_handler = response_use_case.pop(0)
    else:
        result_handler = "Empty"

    return result_handler, 200


@app.route("/use_case_example_cmd", methods=['POST'])
def do_use_case_example_cmd():
    """
    use case example

    + Example test OK:

        curl --header "Content-Type: application/json" --request POST \
             --data '{"name":"xyz1", "operation":"+", "operator":"20"}' \
             http://localhost:5000/use_case_example_cmd

    + Example test KO (send mail):

        curl --header "Content-Type: application/json" --request POST \
             --data '{"name":"xyz1", "operation":"/", "operator":"20"}' \
             http://localhost:5000/use_case_example_cmd

    :return: str
    """
    p_name = request.json['name']
    p_operation = request.json['operation']
    p_operator = int(request.json['operator'])
    current_app.logger.info(f"[*] /use_case_example")
    current_app.logger.info(f"[*] Request: Name={p_name} operation={p_operation} operator={p_operator}")

    try:
        command_action1 = commands.CommandAction1UseCase(
            uuid=uuid.uuid4(),
            name=p_name,
            operation=p_operation,
            operator=p_operator)

        response_use_case = bus.handle(command_action1)

        if len(response_use_case) > 0:
            result_handler = response_use_case.pop(0)

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

    return jsonify({'result': result_handler.resul}), 200


@app.route("/use_case_example_cmd/<id>", methods=['GET'])
def use_case_view_endpoint(id):
    """
    Views entrypoint.

    To test: curl http://localhost:5000/use_case_example_cmd/10

    """
    current_app.logger.info(f"[*] /use_case_example_cmd/<id> Id={id}")
    result = views_cqrs.view_use_case(uuid=id, unit_of_work=bus.uow)
    current_app.logger.info(f"[*] /use_case_example_cmd/<id> Result view={result}")

    if not result:
        return "No data", 404

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)
