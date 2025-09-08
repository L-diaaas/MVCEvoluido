from flask_restx import Namespace, Resource, fields
from flask import request
from controllers.task_controller import TaskController

api = Namespace('tasks', description='Operações CRUD com as Tasks.')

tasks_model = api.model('Task',{
    'id': fields.Integer(reandoly=True, description='ID da task'),
    'title': fields.String(required=True, description='Título da task'),
    'description': fields.String(required=True, description='Descrição da task'),
    'status': fields.String(description='Status ds task (Pendente/Concluido)'),
    'user_id': fields.Integer(required=True, description='Usuário que realizará a task')
})

@api.route('/')
class TaskList(Resource):
    @api.marshal_list_with(tasks_model)
    def get(self):
        return TaskController.list_task()
    
    @api.expect(tasks_model)
    @api.marshal_with(tasks_model, code=201)
    def post(self):
        return TaskController.create_task
    
@api.route('/<int:task_id>')
class Task(Resource):
    @api.marshal_with(tasks_model)
    def put(self, task_id):
            return TaskController.update_task_status(task_id)
        
    def delete(self, task_id):
        return TaskController.delete_task(task_id)
