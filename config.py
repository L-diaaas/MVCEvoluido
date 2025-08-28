import os
#Importa o módulo 'os', que serve para lidar com coisas do sistema operacional
#aqui está sendo usado para gerar uma chave secreta aleatória
class Config:
    #cria uma classe chamada Config para guardar todas as configurações da aplicação
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    #Endereço do banco de dados que o SQLAlchemy vai usar
    #Aqui está apontado para um arquivo SQLite chamado users.db
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #Desliga um recurso do SQLAlchemy que fica rastreando alterações nos objetos
    #Isso economiza memória e evita avisos desnecessário
    SECRET_KEY = os.urandom(24)
    
 
    