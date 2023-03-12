run:
	source ./venv/bin/activate && uvicorn --reload --log-config logging_test.conf {{cookiecutter.module_name}}.routes.base:app

db:
	docker run -d -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust --name db-{{cookiecutter.module_name}} postgres:15
	sleep 3

migrate:
	alembic upgrade head
