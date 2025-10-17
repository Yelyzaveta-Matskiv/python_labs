from abc import ABC, abstractmethod

class Medicine(ABC):
    def __init__(self, name: str, quantity: int, price: float):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")

        self.name = name
        self.quantity = quantity
        self.price = float(price)

    @abstractmethod
    def requires_prescription(self) -> bool:
        pass

    @abstractmethod
    def storage_requirements(self) -> str:
        pass

    def total_price(self) -> float:
        return self.quantity * self.price

    @abstractmethod
    def info(self) -> str:
        pass


class Antibiotic(Medicine):
    def requires_prescription(self) -> bool:
        return True

    def storage_requirements(self) -> str:
        return "8–15°C, dark place"

    def info(self) -> str:
        return (
            f"Antibiotic: {self.name}, Qty: {self.quantity}, "
            f"Total: {self.total_price():.2f}, "
            f"Prescription: {self.requires_prescription()}, "
            f"Storage: {self.storage_requirements()}"
        )


class Vitamin(Medicine):
    def requires_prescription(self) -> bool:
        return False

    def storage_requirements(self) -> str:
        return "15–25°C, dry"

    def info(self) -> str:
        return (
            f"Vitamin: {self.name}, Qty: {self.quantity}, "
            f"Total: {self.total_price():.2f}, "
            f"Prescription: {self.requires_prescription()}, "
            f"Storage: {self.storage_requirements()}"
        )


class Vaccine(Medicine):
    def requires_prescription(self) -> bool:
        return True

    def storage_requirements(self) -> str:
        return "2–8°C, refrigerator"

    def total_price(self) -> float:
        base = super().total_price()
        return base * 1.10  # +10%

    def info(self) -> str:
        return (
            f"Vaccine: {self.name}, Qty: {self.quantity}, "
            f"Total: {self.total_price():.2f}, "
            f"Prescription: {self.requires_prescription()}, "
            f"Storage: {self.storage_requirements()}"
        )