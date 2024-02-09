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
        print(f"Sale: Car - {sale.car.modelo}, User - {sale.user.nome}, Payment Method - {sale.payment_method}")