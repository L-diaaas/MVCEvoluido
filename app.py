import os
from flask import Flask
from config import Config
from swagger.swagger_config import swagger_config 
from controllers.user_controller import UserController 
from controllers.task_controller import TaskController
from models.user import db

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))

app.config.from_object(Config)
swagger_config(app)

db.init_app(app)

with app.app_context():
    db.create_all() 




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5002)
