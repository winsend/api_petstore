from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Order(BaseModel):
    id: Optional[int] = None
    petId: int
    quantity: int = Field(..., gt=0)
    shipDate: Optional[datetime] = None
    status: str = Field(..., pattern="^(placed|approved|delivered)$")
    complete: bool = False

