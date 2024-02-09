from app import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    tabela_fipe = db.Column(db.String(20))
    kilometragem = db.Column(db.Float)
    utilitario = db.Column(db.Boolean)

class User:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf

class Employee:
    def __init__(self, login, nome, cpf, senha, nivel_atendimento):
        self.login = login
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.nivel_atendimento = nivel_atendimento


class Sale:
    def __init__(self, car, user, employee, payment_method):
        self.car = car
        self.user = user
        self.employee = employee
        self.payment_method = payment_method