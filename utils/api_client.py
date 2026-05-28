import requests
import allure

BASE_URL = "https://petstore.swagger.io/v2"

class PetStoreClient:
    
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
    
    @allure.step("Создать питомца")
    def create_pet(self, pet_data):
        response = self.session.post(f"{self.base_url}/pet", json=pet_data)
        return response
    
    @allure.step("Получить питомца по ID")
    def get_pet_by_id(self, pet_id):
        response = self.session.get(f"{self.base_url}/pet/{pet_id}")
        return response
    
    @allure.step("Обновить питомца")
    def update_pet(self, pet_data):
        response = self.session.put(f"{self.base_url}/pet", json=pet_data)
        return response
    
    @allure.step("Удалить питомца")
    def delete_pet(self, pet_id):
        response = self.session.delete(f"{self.base_url}/pet/{pet_id}")
        return response
    
    @allure.step("Найти питомцев по статусу: {status}")
    def find_pets_by_status(self, status: str):
        """Найти питомцев по статусу (available, pending, sold)"""
        response = self.session.get(f"{self.base_url}/pet/findByStatus", params={"status": status})
        return response