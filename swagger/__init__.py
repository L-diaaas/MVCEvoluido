from flask_restx import Api
from flask import Blueprint
from .namespace.users_namespace import api as user_ns
from .namespace.tasks_namespace import api as task_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api (blueprint, doc='/docs', title='Gerenciamento de Tasks', version='0.0.1', description='Api criada para criar e gerenciar Tarefas.')

api.add_namespace(user_ns, path='/users')
api.add_namespace(task_ns, path='/tasks')