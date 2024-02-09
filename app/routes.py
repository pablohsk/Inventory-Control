from flask import request, jsonify
from app import app, db
from app.model import Car, User, Employee, Sale
from app.controller import CarController, UserController, EmployeeController, SaleController
from app.view import CarView, UserView, EmployeeView, SaleView

car_controller = CarController()
user_controller = UserController()
employee_controller = EmployeeController()
sale_controller = SaleController()

car_view = CarView()
user_view = UserView()
employee_view = EmployeeView()
sale_view = SaleView()

@app.route('/create_car', methods=['POST'])
def create_car():
    data = request.get_json()
    car_id = car_controller.create_car(**data)
    return jsonify({"car_id": car_id})

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = user_controller.create_user(**data)
    return jsonify({"user_id": user_id})

@app.route('/create_employee', methods=['POST'])
def create_employee():
    data = request.get_json()
    employee_id = employee_controller.create_employee(**data)
    return jsonify({"employee_id": employee_id})

@app.route('/create_sale', methods=['POST'])
def create_sale():
    data = request.get_json()
    sale_id = sale_controller.create_sale(**data)
    return jsonify({"sale_id": sale_id})