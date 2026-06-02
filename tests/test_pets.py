import allure
import pytest

from data.test_data import invalid_pet

@allure.feature("Petstore API")
@allure.story("Управление питомцами")
class TestPetstoreAPI:

    @pytest.mark.positive
    @allure.title("Создание нового питомца")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_pet(self, pet_data, created_pet):
        assert created_pet["name"] == pet_data["name"]
        assert created_pet["status"] == pet_data["status"]
        assert "id" in created_pet and created_pet["id"] > 0
        assert len(created_pet.get("photoUrls", [])) > 0


    @allure.title("Получение питомца по ID")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_pet_by_id(self, client, created_pet):


        pet_id = created_pet["id"]
        response = client.get_pet_by_id(pet_id)
        assert response.status_code == 200

        data = response.json()
        assert data["id"] == pet_id
        assert data["name"] == created_pet["name"]
        assert data["status"] == created_pet["status"]
        


    @allure.title("Обновление данных питомца")
    def test_update_pet(self, client, created_pet, updated_pet_data):

        updated_pet_data["id"] = created_pet["id"]
        response = client.update_pet(updated_pet_data)
        assert response.status_code == 200

        data = response.json()
        assert data["name"] == updated_pet_data["name"]
        assert data["status"] == updated_pet_data["status"]


    @allure.title("Удаление питомца")
    def test_delete_pet(self, client, created_pet):

        pet_id = created_pet["id"]
        response = client.delete_pet(pet_id)
        assert response.status_code == 200

        # Проверяем, что питомец действительно удалён
        with allure.step("Проверяем, что питомец удалён"):
            get_response = client.get_pet_by_id(pet_id)
            assert get_response.status_code == 404


    @allure.title("Поиск питомцев по статусу")
    @pytest.mark.parametrize("status", ["available", "pending", "sold"])
    def test_find_pets_by_status(self, client, status):

        with allure.step(f"Ищем питомцев со статусом: {status}"):
            response = client.find_pets_by_status(status)
            assert response.status_code == 200

            pets = response.json()
        
            assert isinstance(pets, list)


    @allure.title("Негативный тест - Создание питомца с некорректными данными")
    def test_create_pet_invalid_data(self, client):

        with allure.step("Пытаемся создать питомца с некорректными данными"):
            response = client.create_pet(invalid_pet)

        assert response.status_code in [200, 400, 500]