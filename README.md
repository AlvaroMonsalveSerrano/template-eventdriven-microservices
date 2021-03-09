# Template-eventdriven-microservices

## Introduction

Project example in Python language of an Event-Driven architecture. The producer / consumer broker is used provided by Redis.

All the code defined in the project aims to describe the elements necessary for an architecture event-driven with a didactic ending.


## Work environment creation

### Project

    1.- Creation of the project folder.
    2.- Creation of the virtual environment.
      2.1.- Creation of the environment: $> virtualenv -p python3.6 .venv
      2.2.- Activate the environment: $> source .venv / bin / activate
      2.3.- To deactivate the environment: $> deactivate
    
      The virtual environment is installed in the project's .venv folder.
    
    3.- Installing the dependencies: $> pip install -r requirements.txt

### Redis

For the Redis installation we will use a Docker container. The steps to follow are those:

1.- Download the Redis image.

```
docker pull redis
```

2.- Starting the image.

```
docker container run --name some-redis -d redis
```


## Test

+ Execution of unit tests locally:

```
pytest --setup-show ./tests/unit
```

+ Execution of unit tests in Docker.

```
make unit-tests
```

+ Execution of integration tests with Redis. A docker compose is defined with the different containers needed to
perform the integration tests. To run the integration tests, run the following:

```
make integration-tests
```

## Run

### Local

To start the application locally, it is necessary to have the Docker container running as mentioned in the
previous section. In addition, it is necessary to define the following environment variables: ** ENV ** variable, to define the
runtime environment; and, variable REDIS_HOST, to define the IP of the Redis container.

```
cd entrypoints
export ENV = local
expot REDIS_HOST = 172.17.0.2
export FLASK_APP = app.py
flask run
```

To boot from an IDE like PyCharm, it is only necessary to define the ENV and REDIS_HOST variables.


To test the endpoints, if the application is raised in a local environment on port 5000, the
following curl commands:

```
curl http: // localhost: 5000 /
curl http: // localhost: 5000 / readiness
curl http: // localhost: 5000 / liveness
curl --header "Content-Type: application / json" --request POST \
     --data '{"name": "xyz1", "operation": "+", "operator": "20"}' \
     http: // localhost: 5000 / use_case_example
```

### Docker

A docker compose is defined with three services:

+ **redis.-** Service with the Redis broker.
+ **api.-** Service with the application installed.
+ **consumer_redis.-** Service with the consumer of the Redis broker.

To start operations with Docker, a Makefile is defined with the basic Docker operations:

+ **build** Operation for the creation of the Docker image

```
docker-compose build

> make build
```

+ **up** Operation to start services.
```
docker-compose up -d

> make up
```


+ **test.-** Operation for the execution of the tests.

```
docker-compose run --rm --no-deps --entrypoint = pytest api / app / tests / unit / app / tests / integration / app / tests / e2e

> make test
```


+ **unit-tests.-** Operation for the execution of unit tests.
 
```
docker-compose run --rm --no-deps --entrypoint = pytest api / app / tests / unit

> make unit-tests
```


+ **integration-tests.-** Operation for the execution of integration tests.
 
```
docker-compose run --rm --no-deps --entrypoint = pytest api / app / tests / integration

> make integration-tests
```


+ **e2e-tests.-** Operation for the execution of end to end tests. Not defined.

```
docker-compose run --rm --no-deps --entrypoint = pytest api / app / tests / e2e

> make e2e-tests
```


+ **logs.-** Operation to display the logs of the redis service.

```
docker-compose logs --tail = 25 api redis

> make logs
```


+ **down.-** Operation for the elimination of services.

```
docker-compose down --remove-orphans

> make down
```


+ **all.-** Operation that performs the following: elimination of services, creation of images and startup of
services, that is, it is the union of the following operations: down, build and up.
 
```
down build up

> make all
```
 
To test the endpoints of the application started in the container, the following curl commands can be used:

#### Test curl examples

```
curl http: // localhost: 6060 /
curl http: // localhost: 6060 / liveness
curl http: // localhost: 6060 / rediness
curl --header "Content-Type: application / json" --request POST \
     --data '{"name": "xyz1", "operation": "+", "operator": "20"}' \
     http: // localhost: 6060 / use_case_example_cmd
```

---

# Template-eventdriven-microservices

## Introducción

Ejemplo de proyecto en lenguaje Python de una arquitectura Event-Driven. Se utiliza como broker productor/consumidor el
que proporciona Redis.

Todo el código definido en el proyecto tiene como objetivo describir los elementos necesarios para una arquitectura 
event-driven con una finalizadad didáctica.


## Creación entorno de trabajo

### Proyecto

    1.- Creación de la carpeta del proyecto.
    2.- Creación del entorno virtual.
      2.1.- Creación del entorno: $>virtualenv -p python3.6 .venv
      2.2.- Activar el entorno: $>source .venv/bin/activate
      2.3.- Para desactivar el entorno: $>desactivate
    
      El entorno virtual se instala en la carpeta .venv del proyecto.
    
    3.- Instalación d elas dependencias: $>pip install -r requirements.txt  

### Redis

Para la instalación de Redis emplearemos un contenedor Docker. Los pasos a seguir son los siguientes:

1.- Descarga de la imagen Redis.

```
docker pull redis
```

2.- Arranque de la imagen. 

```
docker container run --name some-redis -d redis
``` 


## Test

+ Ejecución de test unitarios en local:

```
pytest --setup-show ./tests/unit
```

+ Ejecución de test unitarios en Docker.

```
make unit-tests
```

+ Ejecución de test de integración con Redis. Se define un docker compose con los diferentes contenedores necesarios para
realizar los test de integración. Para ejecutar los test de integración se ejecuta lo siguiente:

```
make integration-tests
```

## Run

### Local

Para arrancar la aplicación en local es necesario tener en ejecución el contendor Docker como se ha comentado en el 
apartado anterior. Además, es necesario definir las siguientes variables de entorno: variable **ENV**, para definir el 
entorno de ejecución; y, variable REDIS_HOST, para definir la IP del contenedor de Redis.

```
cd entrypoints
export ENV=local 
expot REDIS_HOST=172.17.0.2
export FLASK_APP=app.py
flask run
```

Para arrancar desde un IDE como PyCharm, solo es necesario definir las variable ENV y REDIS_HOST.



Para probar los endpoint, si se levanta la aplicación en un entorno local en el puerto 5000, se pueden emplear los 
siguiente comandos curl:

```
curl http://localhost:5000/
curl http://localhost:5000/readiness
curl http://localhost:5000/liveness
curl --header "Content-Type: application/json" --request POST \
     --data '{"name":"xyz1", "operation":"+", "operator":"20"}' \
     http://localhost:5000/use_case_example
```

### Docker 

Se define un docker compose con tres servicios: 

+ **redis.-** Servicio con el broker Redis.
+ **api.-** Servicio con la aplicación instalada.
+ **consumer_redis.-** Servicio con el consumidor del broker Redis.

Para arrancar las operaciones con Docker, se define un fichero Makefile con las operaciones básicas de Docker:

+ **build** Operación para la creación de la imagen Docker 
```
docker-compose build

>make build
```

+ **up** Operación para el arranque de los servicios.
```
docker-compose up -d

>make up
```


+ **test.-** Operación para la ejecución de los test.

```
docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/unit /app/tests/integration /app/tests/e2e

>make test
```


+ **unit-tests.-** Operación para la ejecución de los test unitarios.
 
```
docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/unit

>make unit-tests
```


+ **integration-tests.-** Operación para la ejecución de los test de integración.
 
```
docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/integration

>make integration-tests
```


+ **e2e-tests.-** Operación para la ejecución de los test end to end. No definidos.

```
docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/e2e

>make e2e-tests
```


+ **logs.-** Operación para la visualización de los logs del servicio redis.
```
docker-compose logs --tail=25 api redis

>make logs
```


+ **down.-** Operación para la eliminación de los servicios.

```
docker-compose down --remove-orphans

>make down
```


+ **all.-** Operación que realiza los siguiente: eliminación de los servicios, creación de la imágenes y arranque de los
servicios, es decir, es la unión de las siguientes operaciones: down, build y up.
 
``` 
down build up

>make all
```
 


Para probar los endpoints de la aplicación arrancada en el contenedor, se pueden utilizar los siguientes comandos curl:


#### Ejemplos curl de prueba

```
curl http://localhost:6060/
curl http://localhost:6060/liveness
curl http://localhost:6060/rediness
curl --header "Content-Type: application/json" --request POST \
     --data '{"name":"xyz1", "operation":"+", "operator":"20"}' \
     http://localhost:6060/use_case_example_cmd
```

