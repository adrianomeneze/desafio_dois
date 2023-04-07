import pytest
from unittest.mock import MagicMock
from domain.orders import Order
from domain.orders_repositories import Repository
from application.orders import Orders

class TestOrders:
    @pytest.fixture
    
    def test_combine_orders(self):
        repository_mock = MagicMock(spec=Repository)
        orders = Orders(repository_mock)

        requests = [10, 8, 6, 4, 2]
        num_max = 12
        expected_output = 3

        requests.sort = MagicMock()

        assert orders.combine_orders(requests, num_max) == expected_output

        requests.sort.assert_called_once_with(reverse=True)
        
    def test_combine_orders_empty_requests(self):
        repository_mock = MagicMock(spec=Repository)
        orders = Orders(repository_mock)

        requests = []
        num_max = 10

        result = orders.combine_orders(requests, num_max)

        assert result == 0

