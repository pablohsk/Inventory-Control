import re
from app import db
from app.model import Car, User, Employee, Sale

class CarController:
    def create_car(self, modelo, ano, preco, tabela_fipe, kilometragem, utilitario):
        car = Car(modelo=modelo, ano=ano, preco=preco, tabela_fipe=tabela_fipe, kilometragem=kilometragem, utilitario=utilitario)
        db.session.add(car)
        db.session.commit()
        return car.id

    def update_car(self, car_id, **data):
        car = Car.query.get_or_404(car_id)

        # Atualizar os campos conforme necessário
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
            raise ValueError("Formato inválido para CPF. Use xxx.xxx.xxx-xx")
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
    def create_employee(self, login, nome, cpf, senha, nivel_atendimento):
        employee = Employee(login=login, nome=nome, cpf=cpf, senha=senha, nivel_atendimento=nivel_atendimento)
        db.session.add(employee)
        db.session.commit()
        return employee.id

    def update_employee(self, employee_id, **data):
        employee = Employee.query.get_or_404(employee_id)

        # Atualizar os campos conforme necessário
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
        sale = Sale(car_id=car_id, user_id=user_id, employee_id=employee_id, payment_method=payment_method)
        db.session.add(sale)
        db.session.commit()
        return sale.id

    def update_sale(self, sale_id, **data):
        sale = Sale.query.get_or_404(sale_id)

        # Atualizar os campos conforme necessário
        sale.car_id = data.get('car_id', sale.car_id)
        sale.user_id = data.get('user_id', sale.user_id)
        sale.employee_id = data.get('employee_id', sale.employee_id)
        sale.payment_method = data.get('payment_method', sale.payment_method)

        db.session.commit()

        return sale.id