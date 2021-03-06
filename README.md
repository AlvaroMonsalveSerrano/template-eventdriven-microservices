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

## Introducci??n

Ejemplo de proyecto en lenguaje Python de una arquitectura Event-Driven. Se utiliza como broker productor/consumidor el
que proporciona Redis.

Todo el c??digo definido en el proyecto tiene como objetivo describir los elementos necesarios para una arquitectura 
event-driven con una finalizadad did??ctica.


## Creaci??n entorno de trabajo

### Proyecto

    1.- Creaci??n de la carpeta del proyecto.
    2.- Creaci??n del entorno virtual.
      2.1.- Creaci??n del entorno: $>virtualenv -p python3.6 .venv
      2.2.- Activar el entorno: $>source .venv/bin/activate
      2.3.- Para desactivar el entorno: $>desactivate
    
      El entorno virtual se instala en la carpeta .venv del proyecto.
    
    3.- Instalaci??n d elas dependencias: $>pip install -r requirements.txt  

### Redis

Para la instalaci??n de Redis emplearemos un contenedor Docker. Los pasos a seguir son los siguientes:

1.- Descarga de la imagen Redis.

```
docker pull redis
```

2.- Arranque de la imagen. 

```
docker container run --name some-redis -d redis
``` 


## Test

+ Ejecuci??n de test unitarios en local:

```
pytest --setup-show ./tests/unit
```

+ Ejecuci??n de test unitarios en Docker.

```
make unit-tests
```

+ Ejecuci??n de test de integraci??n con Redis. Se define un docker compose con los diferentes contenedores necesarios para
realizar los test de integraci??n. Para ejecutar los test de integraci??n se ejecuta lo siguiente:

```
make integration-tests
```

## Run

### Local

Para arrancar la aplicaci??n en local es necesario tener en ejecuci??n el contendor Docker como se ha comentado en el 
apartado anterior. Adem??s, es necesario definir las siguientes variables de entorno: variable **ENV**, para definir el 
entorno de ejecuci??n; y, variable REDIS_HOST, para definir la IP del contenedor de Redis.

```
cd entrypoints
export ENV=local 
expot REDIS_HOST=172.17.0.2
export FLASK_APP=app.py
flask run
```

Para arrancar desde un IDE como PyCharm, solo es necesario definir las variable ENV y REDIS_HOST.



Para probar los endpoint, si se levanta la aplicaci??n en un entorno local en el puerto 5000, se pueden emplear los 
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
+ **api.-** Servicio con la aplicaci??n instalada.
+ **consumer_redis.-** Servicio con el consumidor del broker Redis.

Para arrancar las operaciones con Docker, se define un fichero Makefile con las operaciones b??sicas de Docker:

+ **build** Operaci??n para la creaci??n de la imagen Docker 
```
docker-compose build

>make build
```

+ **up** Operaci??n para el arranque de los servicios.
```
docker-compose up -d

>make up
```


+ **test.-** Operaci??n para la ejecuci??n de los test.

```
docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/unit /app/tests/integration /app/tests/e2e

>make test
```


+ **unit-tests.-** Operaci??n para la ejecuci??n de los test unitarios.
 
```
docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/unit

>make unit-tests
```


+ **integration-tests.-** Operaci??n para la ejecuci??n de los test de integraci??n.
 
```
docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/integration

>make integration-tests
```


+ **e2e-tests.-** Operaci??n para la ejecuci??n de los test end to end. No definidos.

```
docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/e2e

>make e2e-tests
```


+ **logs.-** Operaci??n para la visualizaci??n de los logs del servicio redis.
```
docker-compose logs --tail=25 api redis

>make logs
```


+ **down.-** Operaci??n para la eliminaci??n de los servicios.

```
docker-compose down --remove-orphans

>make down
```


+ **all.-** Operaci??n que realiza los siguiente: eliminaci??n de los servicios, creaci??n de la im??genes y arranque de los
servicios, es decir, es la uni??n de las siguientes operaciones: down, build y up.
 
``` 
down build up

>make all
```
 


Para probar los endpoints de la aplicaci??n arrancada en el contenedor, se pueden utilizar los siguientes comandos curl:


#### Ejemplos curl de prueba

```
curl http://localhost:6060/
curl http://localhost:6060/liveness
curl http://localhost:6060/rediness
curl --header "Content-Type: application/json" --request POST \
     --data '{"name":"xyz1", "operation":"+", "operator":"20"}' \
     http://localhost:6060/use_case_example_cmd
```

