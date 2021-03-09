build:
	docker-compose build

up:
	docker-compose up -d

test: up
	docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/unit /app/tests/integration /app/tests/e2e

unit-tests: up
	docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/unit

integration-tests: up
	docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/integration

e2e-tests: up
	docker-compose run --rm --no-deps --entrypoint=pytest api /app/tests/e2e

logs:
	docker-compose logs --tail=25 api redis

down:
	docker-compose down --remove-orphans

all: down build up
