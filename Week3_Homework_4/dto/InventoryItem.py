from pydantic import BaseModel, field_validator
from dto.ItemOrigin import ItemOrigin

class InventoryItem(BaseModel):
    name: str
    quantity: int
    serial_num: str
    origin: ItemOrigin