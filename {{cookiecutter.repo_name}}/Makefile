run:
	source ./venv/bin/activate && uvicorn --reload --log-config logging_dev.conf {{cookiecutter.module_name}}.routes.base:app

configure: venv
	source ./venv/bin/activate && pip install -r requirements.dev.txt -r requirements.txt

venv:
	python3.11 -m venv venv

format:
	source ./venv/bin/activate && autoflake -r --in-place --remove-all-unused-imports ./{{cookiecutter.module_name}}
	source ./venv/bin/activate && isort ./{{cookiecutter.module_name}}
	source ./venv/bin/activate && black ./{{cookiecutter.module_name}}
	source ./venv/bin/activate && autoflake -r --in-place --remove-all-unused-imports ./tests
	source ./venv/bin/activate && isort ./tests
	source ./venv/bin/activate && black ./tests
	source ./venv/bin/activate && autoflake -r --in-place --remove-all-unused-imports ./migrations
	source ./venv/bin/activate && isort ./migrations
	source ./venv/bin/activate && black ./migrations

db:
	docker run -d -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust --name db-{{cookiecutter.module_name}} postgres:15

migrate:
	source ./venv/bin/activate && alembic upgrade head
