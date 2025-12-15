
class BusinessLogicError(Exception):
    """Базова помилка бізнес-логіки."""


class ObjectNotFoundError(BusinessLogicError):
    """Об'єкт не знайдено."""


class ValidationError(BusinessLogicError):
    """Некоректні вхідні дані."""


# Перетворення помилки у JSON + HTTP-статус.
def to_error_payload(err: BusinessLogicError) -> tuple[dict, int]:
    if isinstance(err, ObjectNotFoundError):
        return {"error": "not_found", "message": str(err)}, 404
    if isinstance(err, ValidationError):
        return {"error": "validation_error", "message": str(err)}, 400
    return {"error": "business_error", "message": str(err)}, 400