run:
	source ./venv/bin/activate && uvicorn --reload --log-level debug {{cookiecutter.module_name}}.routes.base:app

db:
	docker run -d -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust --name db-{{cookiecutter.module_name}} postgres:15

migrate: db
	alembic upgrade head
