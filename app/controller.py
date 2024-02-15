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