FROM python:3.10
WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

ADD gunicorn_conf.py alembic.ini /app/
ADD migrations /app/migrations
ADD {{cookiecutter.module_name}} /app/{{cookiecutter.module_name}}

CMD [ "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "/app/gunicorn_conf.py", "{{cookiecutter.module_name}}.routes.base:app" ]
