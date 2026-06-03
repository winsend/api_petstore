import requests
import allure

from typing import Union

from models.pet import Pet
from models.order import Order

BASE_URL = "https://petstore.swagger.io/v2"


class PetStoreClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        
    # Методы для питомца
    @allure.step("Создать нового питомца")
    def create_pet(self, pet: Union[Pet, dict]):
        if isinstance(pet, Pet):
            pet = pet.model_dump(exclude_unset=True)
        return self.session.post(f"{self.base_url}/pet", json=pet)

    @allure.step("Получить питомца по ID: {pet_id}")
    def get_pet_by_id(self, pet_id: int):
        return self.session.get(f"{self.base_url}/pet/{pet_id}")

    @allure.step("Обновить данные питомца")
    def update_pet(self, pet: Union[Pet, dict]):
        if isinstance(pet, Pet):
            pet = pet.model_dump()
        return self.session.put(f"{self.base_url}/pet", json=pet)

    @allure.step("Удалить питомца по ID: {pet_id}")
    def delete_pet(self, pet_id: int):
        return self.session.delete(f"{self.base_url}/pet/{pet_id}")

    @allure.step("Найти питомцев по статусу: {status}")
    def find_pets_by_status(self, status: str):
        return self.session.get(f"{self.base_url}/pet/findByStatus", params={"status": status})

    # Методы для заказов
    @allure.step("Создать заказ")
    def create_order(self, order: Union[Order, dict]):
        if isinstance(order, Order):
            order = order.model_dump(mode="json", exclude_unset=True)
        return self.session.post(f"{self.base_url}/store/order", json=order)

    @allure.step("Получить заказ по ID: {order_id}")
    def get_order_by_id(self, order_id: int):
        return self.session.get(f"{self.base_url}/store/order/{order_id}")

    @allure.step("Удалить заказ по ID: {order_id}")
    def delete_order(self, order_id: int):
        return self.session.delete(f"{self.base_url}/store/order/{order_id}")

    @allure.step("Получить inventory")
    def get_inventory(self):
        return self.session.get(f"{self.base_url}/store/inventory")
