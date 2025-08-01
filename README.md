# 📦 case-pod

**Projeto de integração com a API Star Wars (SWAPI), utilizando AWS Lambda e AWS S3 para manipulação e persistência dos dados. Desenvolvido em Python com foco em arquitetura limpa e boas práticas.**

---

## 📑 Sumário

- [Descrição](#descrição)
- [Arquitetura](#arquitetura)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar Localmente](#como-executar-localmente)
- [Autor](#autor)

---

## 📌 Descrição

Este projeto foi desenvolvido como um case técnico, simulando uma arquitetura moderna de microsserviços. O sistema consome dados públicos da **API Star Wars (SWAPI)** e realiza a manipulação dos dados

---

## 🧱 Arquitetura

- **API StarWars (SWAPI)** via GraphQL
- **Função AWS Lambda** que orquestra o fluxo e consome a lógica da aplicação
- **Módulo Python (`case_pod`)** responsável por buscar, processar e formatar os dados
- **AWS S3** para persistência dos dados manipulados

![Diagrama da arquitetura](./diagrama-arquitetura.png)

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- AWS Lambda
- GraphQL (requests)
- SWAPI (https://swapi-graphql.netlify.app/)
- JSON
- Pytest (para testes)
- `requirements.txt` para gerenciamento de dependências

---

## 🛠️ Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/Gabs1993/case-pod.git
cd case-pod

Crie e ative um ambiente virtual: 
python -m venv venv
source venv/bin/activate 

Instale as dependências do projeto:
pip install -r requirements.txt

Execute a simulação: 
python tests/test_lambda.py / Utilizando o Run and Debug


Gabriel Conceição dos Santos / Gabs1993
