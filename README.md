# Petstore API Test Automation Framework

Автоматизированный проект тестирования Swagger Petstore API, реализованный на Python с использованием Pytest, Requests и Allure Report.

## Stack

* Python 3.x
* Pytest
* Requests
* Allure Report
* JSON Schema Validation

## Project Structure

```text
Petstore/
│
├── data/
│   └── test_data.py
│
├── tests/
│   ├── test_pets.py
│   └── test_orders.py
│
├── utils/
│   ├── api_client.py
│   └── schemas.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

## Features

* CRUD операции для Pet API
* CRUD операции для Store Order API
* JSON Schema Validation
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
