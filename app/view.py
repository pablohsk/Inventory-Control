from app.model import Car, User, Employee, Sale

class CarView:
    def display_car_info(self, car):
        print(f"Car: {car.ano} {car.modelo}, Price: {car.preco}")

class UserView:
    def display_user_info(self, user):
        print(f"User: {user.nome}, Email: {user.email}")

class EmployeeView:
    def display_employee_info(self, employee):
        print(f"Employee: {employee.nome}, Level: {employee.nivel_atendimento}")

class SaleView:
    def display_sale_info(self, sale):
        car_model = sale.car.modelo if sale.car else "N/A"
        user_name = sale.user.nome if sale.user else "N/A"
        print(f"Sale: Car - {car_model}, User - {user_name}, Payment Method - {sale.payment_method}")