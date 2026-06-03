# Petstore API Test Automation Framework

Автоматизированный проект тестирования Swagger Petstore API, реализованный на Python с использованием Pytest, Requests и Allure Report.

## Stack

* Python 3.11+
* Pytest
* Requests
* Allure Report
* Pydantic v2
* Faker
* Factory Pattern

## Project Structure
```text
Petstore/
├── factories/           # Фабрики тестовых данных
│   ├── pet_factory.py
│   └── order_factory.py
│
├── models/              # Pydantic модели
│   ├── pet.py
│   └── order.py
│
├── utils/
│   └── api_client.py  
│
├── tests/
│   ├── test_pets.py
│   └── test_orders.py
│
├── conftest.py          # Фикстуры + cleanup
├── requirements.txt
└── README.md
```

## Features

* CRUD операции для Pet API
* CRUD операции для Store Order API
* Allure Reporting
* Pytest Fixtures
* Parametrized Tests
* Positive and Negative Scenarios

## Installation

Clone repository:

```bash
git clone <https://github.com/winsend/api_petstore>
cd Petstore
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest -v
```

## Generate Allure Report

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Implemented Test Cases

### Pet API

* Create Pet
* Get Pet by ID
* Update Pet
* Delete Pet
* Find Pets by Status
* Negative Create Pet

### Store API

* Create Order
* Get Order by ID
* Delete Order
* Get Inventory

## Author

Vlad Lizogub
