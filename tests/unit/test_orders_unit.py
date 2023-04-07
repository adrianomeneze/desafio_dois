import uuid
import pytest

from domain.orders import Order

class TestOrders():
    @pytest.fixture
    
    def test_order_initialized_correctly(self):
        value = 10
        order = Order(value)

        assert isinstance(order.id, str)
        assert len(order.id) == len(str(uuid.uuid4()))
        assert order.value == value
