# Controle de Estoque

## Visão Geral

O Controle de Estoque é uma aplicação web baseada em Flask para gerenciar estoque em uma concessionária de carros.

## Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu_usuario/controle-estoque.git
```
   
2. **Navegue até o diretório do projeto:**
```bash
cd controle-estoque
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Inicialize o banco de dados:**
```bash
flask db init
flask db migrate -m "Inicialização do banco de dados"
flask db upgrade
```

## Estrutura do Projeto
<details>
  <summary><b>controle-estoque</b></summary>
  <ul>
    <li>
      <details>
        <summary><b>app</b></summary>
        <ul>
          <li><code>__init__.py</code>     # Inicialização do aplicativo Flask</li>
          <li><code>models.py</code>       # Definição do modelo de dados</li>
          <li><code>routes.py</code>       # Definição das rotas da API</li>
          <li><code>config.py</code>       # Configurações da aplicação</li>
        </ul>
      </details>
    </li>
    <li><code>tests</code>              # Diretório para testes (opcional)</li>
    <li><code>run.py</code>              # Arquivo para iniciar o aplicativo</li>
    <li><code>requirements.txt</code>    # Lista de dependências</li>
  </ul>
</details>

## Uso

1. **Execute a aplicação:**
```bash
python run.py
Acesse a aplicação em http://localhost:5000 em seu navegador.
```

2. **Crie um carro:**

```bash
  curl -X POST -H "Content-Type: application/json" -d '{"modelo": "ModeloCarro", "ano": 2022, "preco": 50000, "tabela_fipe": "123ABC", "kilometragem": 10000, "utilitario": true}' http://localhost:5000/create_car
```

3. **Crie um usuário:**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"nome": "João Silva", "email": "joao@example.com", "cpf": "123.456.789-00"}' http://localhost:5000/create_user
```

4. **Crie um funcionário:**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"login": "joao_silva", "nome": "João Silva", "cpf": "123.456.789-00", "senha": "senha123", "nivel_atendimento": 1}' http://localhost:5000/create_employee
```

5. **Crie uma venda:**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"car_id": 1, "user_id": 1, "employee_id": 1, "payment_method": "cartao_credito"}' http://localhost:5000/create_sale
```

## Endpoints

Aqui estão os endpoints disponíveis:

```bash
POST /create_car: Cria um novo carro.
POST /create_user: Cria um novo usuário.
POST /create_employee: Cria um novo funcionário.
POST /create_sale: Cria uma nova venda.
```

## Contribuição

Contribuições são bem-vindas! Por favor, envie um pull request com suas alterações.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.
