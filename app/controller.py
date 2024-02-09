from app import db
from app.models import Car, User, Employee, Sale

class CarController:
    def create_car(self, modelo, ano, preco, tabela_fipe, kilometragem, utilitario):
        car = Car(modelo=modelo, ano=ano, preco=preco, tabela_fipe=tabela_fipe, kilometragem=kilometragem, utilitario=utilitario)
        db.session.add(car)
        db.session.commit()
        return car.id

class UserController:
    def create_user(self, nome, email, cpf):
        user = User(nome=nome, email=email, cpf=cpf)
        db.session.add(user)
        db.session.commit()
        return user.id

class EmployeeController:
    def create_employee(self, login, nome, cpf, senha, nivel_atendimento):
        employee = Employee(login=login, nome=nome, cpf=cpf, senha=senha, nivel_atendimento=nivel_atendimento)
        db.session.add(employee)
        db.session.commit()
        return employee.id

class SaleController:
    def create_sale(self, car_id, user_id, employee_id, payment_method):
        sale = Sale(car_id=car_id, user_id=user_id, employee_id=employee_id, payment_method=payment_method)
        db.session.add(sale)
        db.session.commit()
        return sale.id