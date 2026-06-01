from faker import Faker
import random

fake = Faker()


class PetFactory:

    @staticmethod
    def create_data_pet(
        status: str = "available"
    ) -> dict:

        return {
            "id": random.randint(100000, 999999),
            "category": {
                "id": random.randint(1, 100),
                "name": fake.word()
            },
            "name": fake.first_name(),
            "photoUrls": [
                fake.image_url()
            ],
            "tags": [
                {
                    "id": random.randint(1, 100),
                    "name": fake.word()
                }
            ],
            "status": status
        }