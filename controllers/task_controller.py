from flask import render_template, request, redirect, url_for, jsonify
from models.task import Task, db
from models.user import User


class TaskController:
    @staticmethod
    def list_task():
        tasks = Task.query.all()
        task_list = [task.to_dict() for task in tasks]
        return (task_list)
    
    @staticmethod
    def create_task():
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        user_id = data.get('user_id')

        new_task = Task(title=title, description=description, user_id=user_id)
        db.session.add(new_task)
        db.session.commit()
            
        return {
        "message": "Task adicionada com sucesso!",
        "task": {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "status": new_task.status,
            "user_id": new_task.user_id
        }
        }, 201
        
    @staticmethod
    def update_task_status(task_id):
        task = Task.query.get_or_404(task_id)
        task.status = 'Concluído' if task.status == 'Pendente' else 'Pendente'
   
        db.session.commit()
        return {"message": "Status Atualizado.", "task": task.to_dict()}, 200

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {"message": "Task deletada com sucesso."}, 200
    
    
        
