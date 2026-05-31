import requests
import allure
from jsonschema import validate, ValidationError

from utils.schemas import PET_SCHEMA, ORDER_SCHEMA, INVENTORY_SCHEMA


BASE_URL = "https://petstore.swagger.io/v2"


class PetStoreClient:
    """Клиент для работы с Petstore API"""

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

    @allure.step("Создать нового питомца")
    def create_pet(self, pet_data: dict):
        response = self.session.post(f"{self.base_url}/pet", json=pet_data)
        return response

    @allure.step("Получить питомца по ID: {pet_id}")
    def get_pet_by_id(self, pet_id: int):
        response = self.session.get(f"{self.base_url}/pet/{pet_id}")
        return response

    @allure.step("Обновить данные питомца")
    def update_pet(self, pet_data: dict):
        response = self.session.put(f"{self.base_url}/pet", json=pet_data)
        return response

    @allure.step("Удалить питомца по ID: {pet_id}")
    def delete_pet(self, pet_id: int):
        response = self.session.delete(f"{self.base_url}/pet/{pet_id}")
        return response

    @allure.step("Найти питомцев по статусу: {status}")
    def find_pets_by_status(self, status: str):
        response = self.session.get(
            f"{self.base_url}/pet/findByStatus", 
            params={"status": status}
        )
        return response

    # Методы для заказов
    @allure.step("Создать заказ")
    def create_order(self, order_data: dict):
        response = self.session.post(f"{self.base_url}/store/order", json=order_data)
        return response

    @allure.step("Получить заказ по ID: {order_id}")
    def get_order_by_id(self, order_id: int):
        response = self.session.get(f"{self.base_url}/store/order/{order_id}")
        return response

    @allure.step("Удалить заказ по ID: {order_id}")
    def delete_order(self, order_id: int):
        response = self.session.delete(f"{self.base_url}/store/order/{order_id}")
        return response

    @allure.step("Получить inventory")
    def get_inventory(self):
        response = self.session.get(f"{self.base_url}/store/inventory")
        return response

    # JSON Schema Validation
    @allure.step("Валидация JSON по схеме")
    def validate_schema(self, response, schema):
        """Проверяет, соответствует ли ответ JSON Schema"""
        try:
            validate(instance=response.json(), schema=schema)
            allure.attach("JSON Schema validation passed", name="Validation Result", attachment_type=allure.attachment_type.TEXT)
            return True
        except ValidationError as e:
            allure.attach(str(e.message), name="JSON Schema Validation Error", attachment_type=allure.attachment_type.TEXT)
            return False
        except Exception as e:
            allure.attach(str(e), name="Unexpected Error", attachment_type=allure.attachment_type.TEXT)
            return False