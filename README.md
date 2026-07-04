# 💰 Sistema de Controle Financeiro

Um sistema web para gerenciamento financeiro pessoal, desenvolvido com o objetivo de consolidar conhecimentos em desenvolvimento **Full Stack** utilizando **Python, FastAPI, SQLite, HTML, CSS e JavaScript**.

O projeto simula uma aplicação real, permitindo o gerenciamento de receitas, despesas, categorias e metas financeiras, além da geração de relatórios e gráficos.

---

## 📖 Sobre o Projeto

Este projeto foi pensado para servir como uma aplicação completa de estudos, abordando desde a criação de uma API REST até a construção da interface web e integração com banco de dados.

Ao longo do desenvolvimento serão praticados conceitos como:

- Arquitetura de projetos
- Organização de código
- CRUD completo
- APIs REST
- Banco de dados relacional
- Autenticação
- Consumo de APIs
- Manipulação do DOM
- Responsividade
- Deploy

---

# 🚀 Tecnologias

## Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Frontend

- HTML5
- CSS3
- JavaScript

## Ferramentas

- Git
- GitHub
- Uvicorn
- Swagger
- Postman
- VS Code

---

# 📁 Estrutura do Projeto

```text
finance-control/
│
├── app/
│   ├── routers/
│   ├── templates/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   ├── auth.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── database/
│   └── finance.db
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🎯 Objetivos de Aprendizado

Este projeto foi desenvolvido para praticar:

- Organização de projetos profissionais
- APIs REST com FastAPI
- Modelagem de banco de dados
- CRUD completo
- Relacionamentos entre tabelas
- Autenticação de usuários
- Consumo de APIs com JavaScript
- Integração Frontend + Backend
- Manipulação de formulários
- Validação de dados
- Relatórios e gráficos

---

# ✨ Funcionalidades

## 👤 Autenticação

Sistema responsável pelo gerenciamento de usuários.

### Funcionalidades

- Cadastro de usuário
- Login
- Logout
- Criptografia de senha
- Proteção de rotas

### Conceitos praticados

- Hash de senhas
- JWT
- Dependências do FastAPI
- Autenticação

---

## 📊 Dashboard

Tela inicial contendo um resumo financeiro.

### Informações exibidas

- Saldo atual
- Total de receitas
- Total de despesas
- Economia do mês
- Últimas movimentações
- Metas financeiras
- Gráficos

### Conceitos praticados

- Consultas SQL
- Agregações
- Organização da interface

---

## 💵 Receitas

Cadastro das entradas financeiras.

### Operações

- Criar receita
- Editar receita
- Excluir receita
- Listar receitas

### Campos

- Descrição
- Valor
- Categoria
- Data
- Observação

### Conceitos praticados

- CRUD
- Validação
- Formulários

---

## 💳 Despesas

Cadastro das saídas financeiras.

### Operações

- Criar despesa
- Editar despesa
- Excluir despesa
- Listar despesas

### Campos

- Descrição
- Valor
- Categoria
- Forma de pagamento
- Data
- Observação

### Extras

- Parcelamento
- Despesas recorrentes

---

## 🏷 Categorias

Permite organizar receitas e despesas.

### Funcionalidades

- Criar categoria
- Editar categoria
- Excluir categoria

### Exemplos

- Alimentação
- Transporte
- Saúde
- Educação
- Moradia
- Investimentos
- Lazer

### Conceitos praticados

- Relacionamentos
- Foreign Keys

---

## 🎯 Metas Financeiras

Controle de objetivos financeiros.

### Funcionalidades

- Criar meta
- Atualizar progresso
- Excluir meta

### Informações

- Nome
- Valor objetivo
- Valor atual
- Percentual concluído
- Data limite

---

## 📈 Relatórios

Relatórios financeiros personalizados.

### Filtros

- Hoje
- Semana
- Mês
- Ano
- Período personalizado

### Relatórios disponíveis

- Receitas
- Despesas
- Saldo
- Gastos por categoria

### Conceitos praticados

- Queries
- Filtros
- Estatísticas

---

## 🔍 Busca

Pesquisar movimentações utilizando:

- Nome
- Categoria
- Data
- Valor

---

## ↕ Ordenação

Ordenar registros por:

- Data
- Valor
- Categoria
- Mais recente
- Maior valor
- Menor valor

---

## 📄 Paginação

Paginação automática para grandes quantidades de registros.

### Conceitos praticados

- LIMIT
- OFFSET

---

## 👤 Perfil

Permite ao usuário alterar seus dados.

### Funcionalidades

- Alterar nome
- Alterar email
- Alterar senha

---

## ⚙ Configurações

Preferências da aplicação.

### Funcionalidades

- Tema claro
- Tema escuro
- Configuração de moeda

---

## 📤 Exportação

Exportação das movimentações.

### Formatos

- CSV

### Opcional

- PDF

---

## 📊 Gráficos

Visualização dos dados financeiros.

### Exemplos

- Gastos por categoria
- Receitas x Despesas
- Evolução mensal
- Economia por mês

---

# 🗄 Banco de Dados

## users

| Campo | Tipo |
|--------|------|
| id | INTEGER |
| name | TEXT |
| email | TEXT |
| password | TEXT |

---

## categories

| Campo | Tipo |
|--------|------|
| id | INTEGER |
| name | TEXT |

---

## incomes

| Campo | Tipo |
|--------|------|
| id | INTEGER |
| description | TEXT |
| value | REAL |
| date | DATE |
| category_id | INTEGER |
| user_id | INTEGER |

---

## expenses

| Campo | Tipo |
|--------|------|
| id | INTEGER |
| description | TEXT |
| value | REAL |
| date | DATE |
| category_id | INTEGER |
| user_id | INTEGER |

---

## goals

| Campo | Tipo |
|--------|------|
| id | INTEGER |
| name | TEXT |
| target_value | REAL |
| current_value | REAL |
| user_id | INTEGER |

---

# 🌐 API

## Autenticação

| Método | Endpoint |
|---------|----------|
| POST | /register |
| POST | /login |
| GET | /me |

---

## Receitas

| Método | Endpoint |
|---------|----------|
| GET | /incomes |
| GET | /incomes/{id} |
| POST | /incomes |
| PUT | /incomes/{id} |
| DELETE | /incomes/{id} |

---

## Despesas

| Método | Endpoint |
|---------|----------|
| GET | /expenses |
| GET | /expenses/{id} |
| POST | /expenses |
| PUT | /expenses/{id} |
| DELETE | /expenses/{id} |

---

## Categorias

| Método | Endpoint |
|---------|----------|
| GET | /categories |
| POST | /categories |
| PUT | /categories/{id} |
| DELETE | /categories/{id} |

---

## Metas

| Método | Endpoint |
|---------|----------|
| GET | /goals |
| POST | /goals |
| PUT | /goals/{id} |
| DELETE | /goals/{id} |

---

## Relatórios

| Método | Endpoint |
|---------|----------|
| GET | /reports/month |
| GET | /reports/year |
| GET | /reports/category |

---

# 📚 Conceitos Praticados

### Python

- Organização de projetos
- Funções
- Classes
- Tipagem
- Tratamento de exceções

### FastAPI

- Rotas
- Path Parameters
- Query Parameters
- Depends
- Pydantic
- Response Models
- Status Codes
- Middleware
- Autenticação

### Banco de Dados

- SQLite
- SQLAlchemy
- CRUD
- Relacionamentos
- Consultas SQL
- Paginação
- Ordenação
- Filtros

### HTML

- Estrutura semântica
- Formulários
- Templates

### CSS

- Flexbox
- Grid
- Responsividade
- Variáveis CSS

### JavaScript

- DOM
- Eventos
- Fetch API
- Async/Await
- Manipulação dinâmica da interface

---

# 🚧 Melhorias Futuras

- Recuperação de senha
- Upload de foto de perfil
- Notificações
- Controle de cartões de crédito
- Múltiplas contas
- Importação de extratos
- Dashboard mais completo
- Docker
- Testes automatizados
- Deploy em produção

