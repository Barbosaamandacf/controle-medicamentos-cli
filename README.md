# Sistema de Controle de Medicamentos (CLI)

![CI](https://github.com/Barbosaamandacf/controle-medicamentos-cli/actions/workflows/ci.yml/badge.svg)

## Deploy

A aplicação pode ser executada localmente via terminal (CLI).

Repositório: https://github.com/Barbosaamandacf/controle-medicamentos-cli

### Como executar

```bash
git clone https://github.com/Barbosaamandacf/controle-medicamentos-cli.git
cd controle-medicamentos-cli
pip install -r requirements.txt
python main.py
```

---

## Descrição do Problema

Muitas pessoas, especialmente idosos ou pacientes em tratamento contínuo, têm dificuldade em organizar corretamente seus medicamentos, horários, dosagens e duração dos tratamentos. Isso pode causar esquecimentos, uso incorreto e até riscos à saúde.

---

## Proposta da Solução

Este projeto propõe uma aplicação simples em linha de comando (CLI) que permite ao usuário cadastrar, visualizar, editar e remover medicamentos, organizando informações importantes como horário, dosagem e duração do tratamento.

---

## Público-Alvo

- Idosos ou cuidadores
- Pessoas em tratamento contínuo
- Usuários que desejam organizar sua rotina de medicamentos

---

## Funcionalidades Principais

- Cadastro de medicamentos
- Listagem de medicamentos cadastrados
- Edição de informações (nome, dosagem, horário, etc.)
- Remoção de medicamentos
- Armazenamento em arquivo JSON
- Integração com API pública (JSONPlaceholder) para exibir informações externas

---

## Tecnologias Utilizadas

- Python 3
- JSON (armazenamento de dados)
- requests (integração com API pública)

---

## Instruções de Instalação

Clone o repositório:

```bash
git clone https://github.com/Barbosaamandacf/controle-medicamentos-cli.git
```

Acesse a pasta do projeto:

```bash
cd controle-medicamentos-cli
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Instruções de Execução

Execute o arquivo principal:

```bash
python main.py
```

---

## Instruções para Rodar os Testes

Os testes automatizados verificam:

- Criação de medicamentos
- Validação de dosagem inválida
- Validação de nome vazio
- Integração com API pública (teste de integração)

Instale o pytest e execute:

```bash
pip install pytest
pytest
```

---

## Instruções para Rodar o Lint

Instale o flake8 e execute:

```bash
pip install flake8
flake8 .
```

---

## Versão Atual

1.0.0

---

## Autor

Amanda Barbosa

---

## Link do Repositório

https://github.com/Barbosaamandacf/controle-medicamentos-cli