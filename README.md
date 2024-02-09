# Controle de Estoque

## Visão Geral

O Controle de Estoque é uma aplicação web baseada em Flask para gerenciar estoque em uma concessionária de carros.

## Instalação

1. **Clone o repositório:**
```html
<div style="background-color: black; padding: 10px; border-radius: 5px;">
<span style="color: white;">git clone https://github.com/seu_usuario/controle-estoque.git</span>
</div>
```
   
2. **Navegue até o diretório do projeto:**
```html
<div style="background-color: black; padding: 10px; border-radius: 5px;">
  <span style="color: white;">cd controle-estoque</span>
</div>
```

3. **Instale as dependências:**
```html
<div style="background-color: black; padding: 10px; border-radius: 5px;">
  <span style="color: white;">pip install -r requirements.txt</span>
</div>
```

4. **Inicialize o banco de dados:**
```html
<div style="background-color: black; padding: 10px; border-radius: 5px;">
  <span style="color: white;">flask db init</span><br>
  <span style="color: white;">flask db migrate -m "Inicialização do banco de dados"</span><br>
  <span style="color: white;">flask db upgrade</span>
</div>
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
```html
<div style="background-color: black; padding: 10px; border-radius: 5px;">
  <span style="color: white;">python run.py</span><br>
  <span style="color: white;">Acesse a aplicação em <a href="http://localhost:5000" style="color: white; text-decoration: underline;">http://localhost:5000</a> em seu navegador.</span>
</div>
```

2. **Crie um carro:**

```html
<div style="background-color: black; padding: 10px; border-radius: 5px;">
  <span style="color: white;">curl -X POST -H "Content-Type: application/json" -d '{"modelo": "ModeloCarro", "ano": 2022, "preco": 50000, "tabela_fipe": "123ABC", "kilometragem": 10000, "utilitario": true}' http://localhost:5000/create_car</span>
</div>
```

3. **Crie um usuário:**
```html
<div style="background-color: black; padding: 10px; border-radius: 5px;">
  <span style="color: white;">curl -X POST -H "Content-Type: application/json" -d '{"nome": "João Silva", "email": "joao@example.com", "cpf": "123.456.789-00"}' http://localhost:5000/create_user</span>
</div>
```

4. **Crie um funcionário:**
```html
<div style="background-color: black; padding: 10px; border-radius: 5px;">
  <span style="color: white;">curl -X POST -H "Content-Type: application/json" -d '{"login": "joao_silva", "nome": "João Silva", "cpf": "123.456.789-00", "senha": "senha123", "nivel_atendimento": 1}' http://localhost:5000/create_employee</span>
</div>
```

5. **Crie uma venda:**
```html
<div style="background-color: black; padding: 10px; border-radius: 5px;">
  <span style="color: white;">curl -X POST -H "Content-Type: application/json" -d '{"car_id": 1, "user_id": 1, "employee_id": 1, "payment_method": "cartao_credito"}' http://localhost:5000/create_sale</span>
</div>
```

## Endpoints

Aqui estão os endpoints disponíveis:

```html
<div style="background-color: black; padding: 10px; border-radius: 5px;">
  <span style="color: white;">POST /create_car: Cria um novo carro.</span><br>
  <span style="color: white;">POST /create_user: Cria um novo usuário.</span><br>
  <span style="color: white;">POST /create_employee: Cria um novo funcionário.</span><br>
  <span style="color: white;">POST /create_sale: Cria uma nova venda.</span>
</div>
```

## Contribuição

Contribuições são bem-vindas! Por favor, envie um pull request com suas alterações.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.
