from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Cada classe que herda de db.Model se torna uma tabela no banco de dados.
class User(db.Model): # Declaração de um novo modelo/tabela: User
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # Define uma coluna ... 
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }