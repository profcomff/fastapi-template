# {{cookiecutter.repo_name}}

{{cookiecutter.short_description}}

## Запуск

1) Перейдите в папку проекта

2) Создайте виртуальное окружение командой и активируйте его:
```console
foo@bar:~$ python3 -m venv venv
foo@bar:~$ source ./venv/bin/activate  # На MacOS и Linux
foo@bar:~$ venv\Scripts\activate  # На Windows
```

3) Установите библиотеки
```console
foo@bar:~$ pip install -r requirements.txt
```
4) Запускайте приложение!
```console
foo@bar:~$ python -m {{cookiecutter.module_name}}
```

## ENV-file description

DB_DSN=

---
