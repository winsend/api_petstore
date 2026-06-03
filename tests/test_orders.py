import allure
import pytest

from models.order import Order

@allure.feature("Petstore API")
@allure.story("Управление заказами")
class TestPetstoreOrders:

    @allure.title("Создание нового заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order(self,  created_order):
        assert created_order.id is not None
        assert created_order.petId > 0
        assert created_order.quantity > 0
        assert created_order.status == "placed"


    @allure.title("Получение заказа по ID")
    def test_get_order_by_id(self, client, created_order):
        order_id = created_order.id

        with allure.step(f"Получаем заказ по ID: {order_id}"):
            response = client.get_order_by_id(order_id)
            assert response.status_code == 200
            
        order = Order.model_validate(response.json())

        assert created_order.petId == order.petId
        assert created_order.quantity == order.quantity
        assert created_order.status == order.status
        assert created_order.id == order.id

    @allure.title("Удаление заказа")
    def test_delete_order(self, client, created_order):
        order_id = created_order.id

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
        assert len(data) > 0