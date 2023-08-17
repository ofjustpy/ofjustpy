from addict import Dict
from starlette.config import Config

config = Config(".env")
models_pymodule_path = config("models_pymodule", default="models")
user_model_name = config("user_model", default="User")
sqlalchemy_base_name = config("sqlalchemy_base_name", default="Base")

import sys

user_model = None

the_starlette_app = None

mount_route_stack = None

page_builder = None


def load_models():
    global user_model
    try:
        models_pymodule = sys.modules[models_pymodule_path]
        user_model = getattr(models_pymodule, user_model_name)

    except Exception as e:
        print("data model not loaded yet...try again later")
        pass


load_models()


def get_user_model():
    if not user_model:
        load_models()
    if not user_model:
        raise ValueError("No User model found...check configuration")
    return user_model
    pass


def get_sqlalchemy_base():
    Base = getattr(models_pymodule, sqlalchemy_base_name)
    return Base


sa_session = None


def get_sqlalchemy_session():
    return sa_session


def set_sqlalchemy_session(session):
    global sa_session
    sa_session = session


# this needs dependency injection
# no longer needed. oj.build_app takes care of it.
# def set_app(app):
#     global the_starlette_app
#     the_starlette_app = app


def get_app():
    assert the_starlette_app is not None
    return the_starlette_app
