# Teste Técnico

## 📋 Sumário
- [📖 Sobre](#-sobre)
- [🛠 Tecnologias usadas](#-tecnologias-usadas)
- [⚙ Como executar este projeto](#-como-executar-este-projeto)
- [🛠 Endpoints disponíveis](#-endpoints-disponíveis)

## 📖 Sobre
Este projeto é um teste técnico backend.

## 🛠 Tecnologias usadas
Para o desenvolvimento deste projeto as seguintes tecnologias foram usadas:

- python
- Flask

## ⚙ Como executar este projeto
Para funcionar corretamente o indicado é criar uma virtual env

- Criando e executando a virtual env:
``` bash
$ virtualenv venv
$ source venv/bin/activate 
```
- Com a venv ativada instalar as dependências
``` bash
$ pip install -r requirements.txt  
```
- Para rodar a aplicação rodar o seguinte comando
``` bash
$ flask --app app run
```

A aplicação estará rodando na rota:
``` bash
http://localhost:5000/
```

## 🛠 Endpoints disponíveis
Duas rotas estão disponíveis
``` bash
POST
http://localhost:5000/contracts
```
Este endpoint recebe informações dos contratos e retorna de forma ordenada por valor os contratos disponpiveis para negociação. O payload a ser enviado é:
``` bash
{
    "contracts": [
        {
            "id": 1,
            "debt": 40
        }
    ],
    "renegotiated": [3],
    "top_n": 3
}
```
**contracts** é uma lista de objetos, contendo o id do contrato e valor (debt), **renegotiated** é uma lista de ids que já estão em negociação, **top_n** é um inteiro que representa o número de contratos a serem retornados.

O retorno será uma lista contendo o id e o valor dos contratos:
``` bash
[
    "id=5, debt=100",
    "id=4, debt=80",
    "id=1, debt=40"
]
```

``` bash
POST
http://localhost:5000/orders
```
Este endpoint recebe os valores a serem enviados às agências, agrupando em pares e limitando o valor máximo transportado. O payload a ser enviado é:
``` bash
{
    "amount_values": [20, 80, 30],
    "n_max": 80
}
```
**amount_values** é a lista dos valores a serem levados às agências, **n_max** é um inteiro que representa o valor máximo em cada viagem.

O retorno trará o número de viagens necessárias:
``` bash
O número de viagens será: 2
```
