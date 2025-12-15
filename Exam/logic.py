from typing import Dict, List, Optional

from models import ControlledObject
from errors import ObjectNotFoundError, ValidationError

#сервіс для роботи з контрольованими об'єктами.
class ControlledObjectService:
    def __init__(self) -> None:
        self._objects: Dict[int, ControlledObject] = {}
        self._next_id: int = 1

    def list_objects(self) -> List[ControlledObject]:
        return list(self._objects.values())

    def get_object(self, obj_id: int) -> ControlledObject:
        try:
            return self._objects[obj_id]
        except KeyError:
            raise ObjectNotFoundError(f"Object with id {obj_id} not found")

    def create_object(
        self,
        name: str,
        value: float,
        description: Optional[str] = None,
    ) -> ControlledObject:
        self._validate_name(name)
        self._validate_value(value)

        obj = ControlledObject(
            id=self._next_id,
            name=name,
            value=float(value),
            description=description,
        )
        self._objects[self._next_id] = obj
        self._next_id += 1
        return obj

    def update_object(
        self,
        obj_id: int,
        name: Optional[str] = None,
        value: Optional[float] = None,
        description: Optional[str] = None,
    ) -> ControlledObject:
        obj = self.get_object(obj_id)

        if name is not None:
            self._validate_name(name)
            obj.name = name
        if value is not None:
            self._validate_value(value)
            obj.value = float(value)
        if description is not None:
            obj.description = description

        return obj

    def delete_object(self, obj_id: int) -> None:
        if obj_id not in self._objects:
            raise ObjectNotFoundError(f"Object with id {obj_id} not found")
        del self._objects[obj_id]

    # приватні валідатори

    def _validate_name(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValidationError("Field 'name' must be a non-empty string")

    def _validate_value(self, value: float) -> None:
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValidationError("Field 'value' must be a number")

        if value < 0:
            raise ValidationError("Field 'value' must be non-negative")