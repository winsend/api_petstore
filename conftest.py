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



@pytest.fixture(scope="function")
def created_pet(client: PetStoreClient, pet_data):
    """Создаёт питомца и автоматически удаляет его после теста"""
    with allure.step("Создаём питомца для теста"):
        response = client.create_pet(pet_data)
        assert response.status_code == 200

        pet = response.json()
        
        pet_id = pet["id"]
        allure.attach(str(pet_id), name="Created Pet ID", attachment_type=allure.attachment_type.TEXT)

    yield pet  # возвращаем созданного питомца в тест

    # === CLEANUP ===
    with allure.step(f"Cleanup: Удаляем питомца ID={pet_id}"):
        try:
            delete_response = client.delete_pet(pet_id)
            if delete_response.status_code not in (200, 404):
                allure.attach(f"Warning: Delete returned {delete_response.status_code}", 
                             name="Cleanup Warning", 
                             attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            allure.attach(str(e), name="Cleanup Error", attachment_type=allure.attachment_type.TEXT)


@pytest.fixture(scope="function")
def created_order(client: PetStoreClient, order_data):
    """Создаёт заказ и автоматически удаляет его после теста"""
    with allure.step("Создаём заказ для теста"):
        response = client.create_order(order_data)
        assert response.status_code == 200
        order = response.json()
        order_id = order["id"]
        allure.attach(str(order_id), name="Created Order ID", attachment_type=allure.attachment_type.TEXT)

    yield order

    # === CLEANUP ===
    with allure.step(f"Cleanup: Удаляем заказ ID={order_id}"):
        try:
            delete_response = client.delete_order(order_id)
            if delete_response.status_code not in (200, 404):
                allure.attach(f"Warning: Delete order returned {delete_response.status_code}", 
                             name="Cleanup Warning", 
                             attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            allure.attach(str(e), name="Cleanup Error", attachment_type=allure.attachment_type.TEXT)

            
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