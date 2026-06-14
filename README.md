# Sistema de Controle de Medicamentos

## Descrição

O Sistema de Controle de Medicamentos é uma aplicação web desenvolvida em Python com o objetivo de auxiliar usuários no gerenciamento de medicamentos e tratamentos.
A aplicação permite cadastrar, visualizar, atualizar, remover e pesquisar medicamentos, armazenando as informações em um banco de dados PostgreSQL hospedado na nuvem através do Supabase.
O projeto foi desenvolvido durante o projeto de BootCamp II, aplicando conceitos de desenvolvimento colaborativo, integração contínua, banco de dados em nuvem e deploy de aplicações web.

---

## Funcionalidades

* Cadastro de medicamentos
* Listagem de medicamentos
* Atualização de informações
* Remoção de medicamentos
* Pesquisa de medicamentos
* Integração com banco de dados PostgreSQL (Supabase)
* Interface web desenvolvida com Flask
* Deploy em ambiente de produção
* Testes automatizados
* Integração contínua com GitHub Actions

---

## Tecnologias Utilizadas

* Python 3
* Flask
* PostgreSQL
* Supabase
* Git
* GitHub
* GitHub Actions
* Gunicorn
* Pytest
* Flake8
* Bootstrap 5

---

## Banco de Dados

A aplicação utiliza PostgreSQL hospedado no Supabase para armazenamento persistente das informações dos medicamentos.

As operações implementadas incluem:

* Create (Cadastrar)
* Read (Consultar)
* Update (Atualizar)
* Delete (Remover)

---

## Como Executar Localmente

Clone o repositório:

```bash
git clone https://github.com/Barbosaamandacf/controle-medicamentos-cli.git
```

Entre na pasta do projeto:

```bash
cd controle-medicamentos-cli
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure a variável de ambiente DATABASE_URL no arquivo .env.

Execute a aplicação:

```bash
python app.py
```

---

## Testes

Para executar os testes:

```bash
pytest
```

---

## Verificação de Código

Para executar o Flake8:

```bash
flake8 .
```

---

## Deploy

Aplicação publicada em:

https://controle-medicamentos-cli.onrender.com

---

## Repositório

https://github.com/Barbosaamandacf/controle-medicamentos-cli

---

## Integrantes

* Amanda Celina Fernandes Barbosa — RA: 22552352
* Paulo Vitor Sousa – RA: 22551341

---

## Trabalho Colaborativo

O desenvolvimento foi realizado utilizando GitHub com:

* Branches de desenvolvimento
* Pull Requests
* Code Review
* GitHub Actions
* Controle de versão com Git

Cada integrante realizou contribuições individuais através de commits e Pull Requests revisados e integrados à branch principal.
