from flask import request, jsonify
from app import app, db
from app.model import Car, User, Employee, Sale
from app.controller import CarController, UserController, EmployeeController, SaleController
from app.view import CarView, UserView, EmployeeView, SaleView
from flask import render_template

car_controller = CarController()
user_controller = UserController()
employee_controller = EmployeeController()
sale_controller = SaleController()

car_view = CarView()
user_view = UserView()
employee_view = EmployeeView()
sale_view = SaleView()

@app.route
def index():
    return render_template('index.html')

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

@app.route('/update_car/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.get_json()
    updated_car_id = car_controller.update_car(car_id, **data)
    return jsonify({"updated_car_id": updated_car_id})

@app.route('/delete_car/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    deleted_car_id = car_controller.delete_car(car_id)
    return jsonify({"deleted_car_id": deleted_car_id})

@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user_id = user_controller.update_user(user_id, **data)
    return jsonify({"updated_user_id": updated_user_id})

@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted_user_id = user_controller.delete_user(user_id)
    return jsonify({"deleted_user_id": deleted_user_id})

@app.route('/update_employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.get_json()
    updated_employee_id = employee_controller.update_employee(employee_id, **data)
    return jsonify({"updated_employee_id": updated_employee_id})

@app.route('/delete_employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    deleted_employee_id = employee_controller.delete_employee(employee_id)
    return jsonify({"deleted_employee_id": deleted_employee_id})

@app.route('/update_sale/<int:sale_id>', methods=['PUT'])
def update_sale(sale_id):
    data = request.get_json()
    updated_sale_id = sale_controller.update_sale(sale_id, **data)
    return jsonify({"updated_sale_id": updated_sale_id})