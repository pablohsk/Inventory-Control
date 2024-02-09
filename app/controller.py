from app.model import Car, User, Employee, Sale

class CarController:
    def create_car(self, modelo, ano, preco, tabela_fipe, kilometragem, utilitario):
        car = Car(modelo, ano, preco, tabela_fipe, kilometragem, utilitario)
        return car

class UserController:
    def create_user(self, nome, email, cpf):
        user = User(nome, email, cpf)
        return user

class EmployeeController:
    def create_employee(self, login, nome, cpf, senha, nivel_atendimento):
        employee = Employee(login, nome, cpf, senha, nivel_atendimento)
        return employee

class SaleController:
    def create_sale(self, car, user, employee, payment_method):
        sale = Sale(car, user, employee, payment_method)
        return sale