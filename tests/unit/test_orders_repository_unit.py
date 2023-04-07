import pytest
from unittest.mock import MagicMock
from infrastructure.repositories import OrderRepository
from domain.orders import Order


class TestordersRepository():
    @pytest.fixture

    def order_repository(self):
        return OrderRepository()


    def test_create_order(self, order_repository):
        mock_order = MagicMock(spec=Order)
        mock_order.id = "abc123"
        order_repository.create(mock_order)
        assert len(order_repository.orders) == 1
        assert order_repository.orders[0] == mock_order


    def test_read_order(self, order_repository):
        mock_order = MagicMock(spec=Order)
        mock_order.id = "abc123"
        order_repository.orders.append(mock_order)
        result = order_repository.read(mock_order.id)
        assert result == mock_order


    def test_read_order_not_found(self, order_repository):
        with pytest.raises(ValueError):
            order_repository.read("ID not found!")


    def test_update_order(self, order_repository):
        mock_order = MagicMock(spec=Order)
        mock_order.id = "abc123"
        order_repository.orders.append(mock_order)
        mock_updated_order = MagicMock(spec=Order)
        mock_updated_order.id = "abc123"
        order_repository.update(mock_updated_order)
        assert order_repository.orders[0] == mock_updated_order


    def test_update_order_not_found(self, order_repository):
        mock_order = MagicMock(spec=Order)
        mock_order.id = "abc123"
        with pytest.raises(ValueError):
            order_repository.update(mock_order)


    def test_delete_order(self, order_repository):
        mock_order = MagicMock(spec=Order)
        mock_order.id = "abc123"
        order_repository.orders.append(mock_order)
        order_repository.delete(mock_order.id)
        assert len(order_repository.orders) == 0


    def test_delete_order_not_found(self, order_repository):
        with pytest.raises(ValueError):
            order_repository.delete("ID not found!")


    def test_read_all_orders(self, order_repository):
        mock_order1 = MagicMock(spec=Order)
        mock_order1.id = "abc123"
        mock_order2 = MagicMock(spec=Order)
        mock_order2.id = "def456"
        order_repository.orders.append(mock_order1)
        order_repository.orders.append(mock_order2)
        result = order_repository.read_all()
        assert result == [mock_order1, mock_order2]


    def test_read_all_value_of_orders(self, order_repository):
        mock_order1 = MagicMock(spec=Order)
        mock_order1.id = "abc123"
        mock_order1.value = 100
        mock_order2 = MagicMock(spec=Order)
        mock_order2.id = "def456"
        mock_order2.value = 200
        order_repository.orders.append(mock_order1)
        order_repository.orders.append(mock_order2)
        result = order_repository.read_all_value_of_orders()
        assert result == [100, 200]
