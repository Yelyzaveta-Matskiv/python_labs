from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

#Контрольований об'єкт даних Farma Inc.
@dataclass
class ControlledObject:
    id: int
    name: str
    value: float
    created_at: datetime = field(default_factory=datetime.utcnow)
    description: Optional[str] = None

# JSON-формат відповіді
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "created_at": self.created_at.isoformat() + "Z",
            "description": self.description,
        }