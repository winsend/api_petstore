import pytest
import allure
from utils.api_client import PetStoreClient
from factories.pet_factory import PetFactory
from factories.order_factory import OrderFactory



@pytest.fixture(scope="session")
def client():
    client = PetStoreClient()
    yield client


@pytest.fixture(scope="function")
def created_pet(client: PetStoreClient):
    pet = PetFactory.create(status="available")
    
    with allure.step("Создаём питомца для теста"):
        response = client.create_pet(pet)
        assert response.status_code == 200, f"Failed to create pet: {response.text}"
        
        created_data = response.json()
        pet_id = created_data["id"]
        allure.attach(str(pet_id), name="Created Pet ID", attachment_type=allure.attachment_type.TEXT)

        pet = pet.model_copy(update={"id": pet_id})

        allure.attach(str(pet_id), name="Created Pet ID", attachment_type=allure.attachment_type.TEXT)

    yield pet  

    
    with allure.step(f"Cleanup: Удаляем питомца ID={pet_id}"):
        try:
            client.delete_pet(pet_id)
        except Exception as e:
            allure.attach(str(e), name="Cleanup Error", attachment_type=allure.attachment_type.TEXT)




@pytest.fixture(scope="function")
def created_order(client: PetStoreClient):
    order = OrderFactory.create(status="placed")
    order_id = None

    with allure.step("Создаём заказ для теста"):
        response = client.create_order(order)
        
        if response.status_code != 200:
            allure.attach(response.text[:1000], name="Create Order Error Response", attachment_type=allure.attachment_type.TEXT)
        
        assert response.status_code == 200, f"Не удалось создать заказ: {response.status_code} - {response.text[:400]}"
        
        created_data = response.json()
        order_id = created_data.get("id")
        assert order_id is not None, "В ответе нет ID заказа"

        order = order.model_copy(update={"id": order_id})

        allure.attach(str(order_id), name="Created Order ID", attachment_type=allure.attachment_type.TEXT)

    yield order

    if order_id:
        with allure.step(f"Cleanup: Удаляем заказ {order_id}"):
            try:
                client.delete_order(order_id)
            except:
                pass

            

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



def pytest_configure(config):
    config._metadata = {
        "Project": "Petstore API",
        "Framework": "Pytest + Requests + Pydantic",
        "Author": "Влад Лизогуб"
    }