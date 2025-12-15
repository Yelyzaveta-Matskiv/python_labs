import pytest
from datetime import datetime

from logic import ControlledObjectService
from errors import ObjectNotFoundError, ValidationError


def test_create_object_success():
    service = ControlledObjectService()

    obj = service.create_object(name="Test", value=10.5, description="desc")

    assert obj.id == 1
    assert obj.name == "Test"
    assert obj.value == 10.5
    assert obj.description == "desc"
    assert isinstance(obj.created_at, datetime)


def test_create_object_empty_name():
    service = ControlledObjectService()

    with pytest.raises(ValidationError):
        service.create_object(name="", value=1.0)


def test_create_object_invalid_value_type():
    service = ControlledObjectService()

    with pytest.raises(ValidationError):
        service.create_object(name="Ok", value="not-a-number")


def test_create_object_negative_value():
    service = ControlledObjectService()

    with pytest.raises(ValidationError):
        service.create_object(name="Ok", value=-1)


def test_get_object_not_found():
    service = ControlledObjectService()

    with pytest.raises(ObjectNotFoundError):
        service.get_object(999)


def test_update_object_success():
    service = ControlledObjectService()
    obj = service.create_object(name="Old", value=1.0)

    updated = service.update_object(obj.id, name="New", value=2.0, description="upd")

    assert updated.id == obj.id
    assert updated.name == "New"
    assert updated.value == 2.0
    assert updated.description == "upd"


def test_update_object_not_found():
    service = ControlledObjectService()

    with pytest.raises(ObjectNotFoundError):
        service.update_object(123, name="New")


def test_delete_object_success():
    service = ControlledObjectService()
    obj = service.create_object(name="To delete", value=3.0)

    service.delete_object(obj.id)

    with pytest.raises(ObjectNotFoundError):
        service.get_object(obj.id)


def test_delete_object_not_found():
    service = ControlledObjectService()

    with pytest.raises(ObjectNotFoundError):
        service.delete_object(999)