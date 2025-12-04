import pytest
from order import Order

@pytest.fixture
def sample_dict_items():
    return [
        {"name": "apple", "price": 10.0, "quantity": 2},
        {"name": "banana", "price": 5.0, "quantity": 4},
        {"name": "cherry", "price": 20.0, "quantity": 1},
    ]

def test_order_total(sample_dict_items):
    order = Order(id=1, items=sample_dict_items)
    assert order.total() == 60.0  

def test_order_most_expensive(sample_dict_items):
    order = Order(id=1, items=sample_dict_items)
    assert order.most_expensive()["name"] == "cherry"

def test_order_apply_discount_valid(sample_dict_items):
    order = Order(id=1, items=sample_dict_items)
    order.apply_discount(50)
    assert sample_dict_items[0]["price"] == pytest.approx(5.0)
    assert sample_dict_items[1]["price"] == pytest.approx(2.5)
    assert sample_dict_items[2]["price"] == pytest.approx(10.0)

@pytest.mark.parametrize("invalid", [-10, 150])
def test_order_apply_discount_invalid(sample_dict_items, invalid):
    order = Order(id=1, items=sample_dict_items)
    with pytest.raises(ValueError):
        order.apply_discount(invalid)

def test_order_repr(sample_dict_items):
    order = Order(id=42, items=sample_dict_items)
    assert repr(order) == "<Order 42: 3 items>"