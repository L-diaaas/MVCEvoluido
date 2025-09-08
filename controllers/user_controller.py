from flask import render_template, request, redirect, url_for, jsonify
from models.user import User, db

class UserController:
    @staticmethod
    def index():
        users = User.query.all()
        users_list = [user.to_dict() for user in users]
        return (users_list)

    @staticmethod
    def contact():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return {"message":"Usuário criado com sucesso!",
                "user": {
                    'id': new_user.id,
                    'nome': new_user.name,
                    'email': new_user.email
                }}, 201

