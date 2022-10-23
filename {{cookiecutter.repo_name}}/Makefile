run:
	source ./venv/bin/activate && uvicorn --reload --log-level debug {{cookiecutter.module_name}}.routes.base:app

db:
	docker compose up -d

migrate:
	alembic upgrade head
