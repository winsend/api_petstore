import allure
import pytest

from factories.order_factory import OrderFactory
from data.test_data import invalid_pet



@allure.feature("Petstore API")
@allure.story("Управление заказами")
class TestPetstoreOrders:
    
    @allure.title("Создание нового заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order(self, client, order_data):

        with allure.step("Создаём новый заказ"):
            response = client.create_order(order_data)

        with allure.step("Проверяем ответ"):
            assert response.status_code == 200

            data = response.json()

            assert data["petId"] == order_data["petId"]
            assert data["quantity"] == order_data["quantity"]
            assert data["status"] == order_data["status"]


    @allure.title("Получение заказа по ID")
    def test_get_order_by_id(self, client, order_data):
    
        with allure.step("Создаем новый заказ"):
            response = client.create_order(order_data)
            order_id = response.json()["id"]

        with allure.step(f"Получаем заказ по ID: {order_id}"):
            response = client.get_order_by_id(order_id)
        assert response.status_code == 200

        data = response.json()

        assert data["id"] == order_id
        assert data["petId"] == order_data["petId"]


    @allure.title("Удаление заказа")
    def test_delete_order(self, client, order_data):
        
        with allure.step("Создаем новый заказ"):
            response = client.create_order(order_data)
            order_id = response.json()["id"]

        with allure.step(f"Удаляем заказ с ID: {order_id}"):
            response = client.delete_order(order_id)

            assert response.status_code == 200

        with allure.step("Проверяем, что заказ больше не существует"):
            get_response = client.get_order_by_id(order_id)
            assert get_response.status_code == 404


    @allure.title("Получение количества питомцев в магазине")
    def test_get_inventory(self, client):
        with allure.step("Запрашиваем статусы питомцев в магазине"):
            response = client.get_inventory()

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        # Проверяем, что есть хотя бы один статус
        assert len(data) > 0