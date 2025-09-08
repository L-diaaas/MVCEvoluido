from flask_restx import Namespace, Resource, fields
from flask import request
from controllers.user_controller import UserController

api = Namespace('users', description='Listagem e Criação de usuários.')

users_model = api.model('User',{
    'id': fields.Integer(reandoly=True, description='ID do usuário'),
    'nome': fields.String(required=True, description="Nome do usuário"),
    'email': fields.String(required=True, description="Email do usuário")
})

@api.route('/')
class UserList(Resource):
    @api.marshal_list_with(users_model)
    def get(self):
        return UserController.index()
    
    @api.expect(users_model)
    @api.marshal_with(users_model, code=201)
    def post(self):
        return UserController.contact()
    