from app import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    tabela_fipe = db.Column(db.String(20))
    kilometragem = db.Column(db.Float)
    utilitario = db.Column(db.Boolean)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    nivel_atendimento = db.Column(db.Integer, nullable=False)

class Sale:
    def __init__(self, car, user, employee, payment_method):
        self.car = car
        self.user = user
        self.employee = employee
        self.payment_method = payment_method