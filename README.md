# Шаблон для fastapi проекта

## Использование
1) Установите cookiecutter 
```console
foo@bar:~$ pip install cookiecutter
```

2) Перейдите в ту директорию, где у вас будет хранится код для проекта
Это делается комадами:
```console
foo@bar:~$ cd
foo@bar:~$ pwd
foo@bar:~$ ls
```
Это _не_ последовательность команд, а _список_ нужных

Гуглите их, если у вас будет что-то не получаться

3) Выполните раскатку шаблона в текущую директорию командой
```console
foo@bar:~$ cookiecutter https://github.com/profcomff/fastapi-template.git
```

После команды вас спросят, хотите ли вы загрузить шаблон, согласитесь.

Вам зададут несколько вопросов:

    3.1) repo_name - имя будущего репозитория

    3.2) module_name - имя модуля, который будет запускаться командой: python3 -m module_name. На одном уровне с ним будут лежать Dockerfile, .gitignore, .env, Makefile, docker-compose, pyproject.toml, flake8.conf, README.md, requirements.txt, alembic.ini, gunicorn.conf, миграции. А внутри будет лежать исполняемый код.

    3.3) description - Краткое описание проекта для README.md

4) У вас создастся структура проекта, корнем которой будет папка repo_name. Вы должны создать новый пустой репозиторий на GitHub и импортировать туда все из этой папки.

## Стек технологий в шаблоне

1) fastapi
2) sqlalchemy
3) pydantic
4) alembic

Вы можете добавлять новые технологии в файле requirements.txt.

## Предложения по шаблону

Писать мне @Alevardo (tg) или в нашем чатике
