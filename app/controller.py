import re
from flask import g, Flask
from app import db
from app.model import Car, User, Employee, Sale, SaleCar

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/site.db'
app.app_context().push()

class CarController:
    def create_car(self, modelo, ano, preco, tabela_fipe, kilometragem, utilitario):
        car = Car(modelo=modelo, ano=ano, preco=preco, tabela_fipe=tabela_fipe, kilometragem=kilometragem, utilitario=utilitario)
        db.session.add(car)
        db.session.commit()
        return car.id

    def update_car(self, car_id, **data):
        car = Car.query.get_or_404(car_id)

        car.modelo = data.get('modelo', car.modelo)
        car.ano = data.get('ano', car.ano)
        car.preco = data.get('preco', car.preco)
        car.tabela_fipe = data.get('tabela_fipe', car.tabela_fipe)
        car.kilometragem = data.get('kilometragem', car.kilometragem)
        car.utilitario = data.get('utilitario', car.utilitario)

        db.session.commit()

        return car.id

    def delete_car(self, car_id):
        car = Car.query.get_or_404(car_id)

        db.session.delete(car)
        db.session.commit()

        return car.id

class UserController:
    def create_user(self, nome, email, cpf):
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            raise ValueError("Formato inválido para CPF. Ex: 888.777.666-55")
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValueError("Formato inválido para e-mail. Ex: josedasilva@gmail.com")
        user = User(nome=nome, email=email, cpf=cpf)
        db.session.add(user)
        db.session.commit()
        return user.id

    def update_user(self, user_id, **data):
        user = User.query.get_or_404(user_id)
        user.nome = data.get('nome', user.nome)
        user.email = data.get('email', user.email)
        user.cpf = data.get('cpf', user.cpf)

        db.session.commit()

        return user.id

    def delete_user(self, user_id):
        user = User.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()

        return user.id

class EmployeeController:
    def create_employee(self, login, nome, cpf, senha, nivel_atendimento, role):
        allowed_roles = ["atendente", "supervisor"]
        if role.lower() not in allowed_roles:
            raise ValueError("Função Inválida. Use atendente ou supervisor.")
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            raise ValueError("Formato inválido para CPF. Ex: 888.777.666-55")
        employee = Employee(login=login, nome=nome, cpf=cpf, senha=senha, nivel_atendimento=nivel_atendimento, role=role)
        db.session.add(employee)
        db.session.commit()
        return employee.id

    def update_employee(self, employee_id, **data):
        employee = Employee.query.get_or_404(employee_id)

        employee.login = data.get('login', employee.login)
        employee.nome = data.get('nome', employee.nome)
        employee.cpf = data.get('cpf', employee.cpf)
        employee.senha = data.get('senha', employee.senha)
        employee.nivel_atendimento = data.get('nivel_atendimento', employee.nivel_atendimento)

        db.session.commit()

        return employee.id

    def delete_employee(self, employee_id):
        employee = Employee.query.get_or_404(employee_id)

        db.session.delete(employee)
        db.session.commit()

        return employee.id

class SaleController:
    def create_sale(self, car_id, user_id, employee_id, payment_method):
        allowed_payment_methods = ["dinheiro", "débito", "crédito", "pix"]
        if payment_method.lower() not in allowed_payment_methods:
            raise ValueError("Método de pagamento inválido. Use dinheiro, débito, crédito ou pix.")

        sale = Sale(car_id=car_id, user_id=user_id, employee_id=employee_id, payment_method=payment_method)
        db.session.add(sale)
        db.session.commit()
        return sale.id

    def update_sale(self, sale_id, **data):
        if g.employee.role.lower() != "supervisor":
            return {"Error": "Somente supervisores podem atualizar vendas, chame seu supervisor!"}, 403

        sale = Sale.query.get_or_404(sale_id)

        sale.car_id = data.get('car_id', sale.car_id)
        sale.user_id = data.get('user_id', sale.user_id)
        sale.employee_id = data.get('employee_id', sale.employee_id)
        sale.payment_method = data.get('payment_method', sale.payment_method)

        db.session.commit()

        return sale.id

    def create_sale(self, car_id, user_id, employee_id, payment_method):
        sale = Sale(car_id=car_id, user_id=user_id, employee_id=employee_id, payment_method=payment_method)
        db.session.add(sale)
        db.session.commit()
        sale_car = SaleCar(sale_id=sale.id, car_id=car_id)
        db.session.add(sale_car)
        db.session.commit()

        return sale.id