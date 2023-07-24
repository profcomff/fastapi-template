import uvicorn
from {{cookiecutter.module_name}}.routes.base import app

if __name__ == '__main__':
    uvicorn.run(app)
