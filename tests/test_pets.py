import allure
import pytest

from data.test_data import invalid_pet
from models.pet import Pet

from models.pet import Pet

@allure.feature("Petstore API")
@allure.story("Управление питомцами")
class TestPetstoreAPI:


    @allure.title("Создание нового питомца")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_pet(self, created_pet):
        
        assert created_pet.id is not None
        assert created_pet.name
        assert created_pet.status == "available"

    @allure.title("Получение питомца по ID")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_pet_by_id(self, client, created_pet):
        response = client.get_pet_by_id(created_pet.id)
        assert response.status_code == 200

        pet = Pet.model_validate(response.json())

        assert pet.id == created_pet.id
        assert pet.name == created_pet.name
        assert pet.status == created_pet.status

        assert pet.id == created_pet.id
        assert pet.name == created_pet.name
        assert pet.status == created_pet.status

  
    @allure.title("Обновление данных питомца")
    def test_update_pet(self, client, created_pet):
        updated_data = {
            "id": created_pet.id,
            "name": created_pet.name + " Updated",
            "status": "sold"
        }

        response = client.update_pet(updated_data)
        assert response.status_code == 200

        pet = Pet.model_validate(response.json())

        assert pet.id == created_pet.id
        assert pet.name == updated_data["name"]
        assert pet.status == "sold"

    @allure.title("Удаление питомца")
    def test_delete_pet(self, client, created_pet):
        response = client.delete_pet(created_pet.id)
        assert response.status_code == 200

        with allure.step("Проверяем, что питомец удалён"):
            get_response = client.get_pet_by_id(created_pet.id)
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

        