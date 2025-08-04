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

- **API StarWars (SWAPI)** 
- **Função AWS Lambda** 
- **Módulo Python (`case_pod`)** 
- **AWS S3** 

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- AWS Lambda
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

obs: no arquivo local_test já possui as informações para testar, ex: "people: Luke Skywalker" é só rodar com o comando acima ou utilizando o debug

Para executar os testes, você pode ir até: C:\Users\pichau\Case_POD\tests e rodar com o comando: pytest test_swapi_repository.py
ou executar: pytest que vai rodar todos os testes do projeto


Gabriel Conceição dos Santos / Gabs1993
