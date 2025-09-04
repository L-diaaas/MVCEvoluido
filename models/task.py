from models.user import db, User 

class Task(db.Model): 
    __tablename__ = 'tasks' 
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pendente')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

    def __init__(self, title, description, user_id, status="Pendente"):
        self.title = title
        self.description = description
        self.status = status
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'user_id': self.user_id
        }


     
    