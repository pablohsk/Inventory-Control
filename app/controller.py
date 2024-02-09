from app.model import Car, User, Employee, Sale

class CarController:
    def create_car(self, modelo, ano, preco, tabela_fipe, kilometragem, utilitario):
        car = Car(modelo, ano, preco, tabela_fipe, kilometragem, utilitario)
        return car