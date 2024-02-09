class Car:
    def __init__(self, modelo, ano, preco, tabela_fipe, kilometragem, utilitario):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.tabela_fipe = tabela_fipe
        self.kilometragem = kilometragem
        self.utilitario = utilitario

        class User:
            def __init__(self, nome, email, cpf):
                self.nome = nome
                self.email = email
                self.cpf = cpf

        class Employee:
            def __init__(self, login, nome, cpf, senha, nivel_atendimento):
                self.login = login
                self.nome = nome
                self.cpf = cpf
                self.senha = senha
                self.nivel_atendimento = nivel_atendimento

        class Sale:
            def __init__(self, car, user, employee, payment_method):
                self.car = car
                self.user = user
                self.employee = employee
                self.payment_method = payment_method