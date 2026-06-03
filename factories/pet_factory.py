from faker import Faker
from models.pet import Pet, Category, Tag
import random

fake = Faker()

class PetFactory:
    
    @staticmethod
    def create(status: str = "available") -> Pet:
        return Pet(
            name = fake.first_name(),
            category = Category(id=random.randint(1, 100), name=fake.word()),
            photoUrls = [fake.image_url()],
            tags = [Tag(id=random.randint(1, 50), name=fake.word())],
            status = status
        )

    @staticmethod
    def create_dict(status: str = "available", **kwargs) -> dict:
        pet = PetFactory.create(status=status)
        if kwargs:
            pet = pet.model_copy(update=kwargs)
        return pet.model_dump()