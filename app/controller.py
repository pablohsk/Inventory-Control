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
        # Lógica para adicionar ao banco de dados ou outra ação necessária
        return employee
