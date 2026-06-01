import pytest
import allure
from utils.api_client import PetStoreClient
from factories.pet_factory import PetFactory
from factories.order_factory import OrderFactory

# Фикстура для API клиента
@pytest.fixture(scope="session")
def client():
    """Создаёт экземпляр API клиента для всех тестов"""
    client = PetStoreClient()
    yield client

@pytest.fixture
def pet_data():
    return PetFactory.create_data_pet()

@pytest.fixture
def updated_pet_data():
    return PetFactory.create_data_pet(status="sold")

@pytest.fixture
def order_data():
    return OrderFactory.create_data_order()

@pytest.fixture
def updated_order_data():
    return OrderFactory.create_data_order(status="closed")


# Хук для Allure — скриншоты/логи при падении (для API не скриншоты, но полезная информация)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            allure.attach(
                f"Test failed: {report.longrepr.text if hasattr(report.longrepr, 'text') else str(report.longrepr)}",
                name="Error Details",
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception:
            pass


# Настройка Allure
def pytest_configure(config):
    config._metadata = {
        "Project": "Petstore API",
        "Framework": "Pytest + Requests",
        "Author": "Влад Лизогуб"
    }