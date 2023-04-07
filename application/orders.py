from typing import List

from domain.orders import Order
from domain.orders_repositories import Repository


class Orders:
    def __init__(self, order_repository: Repository):
        self.order_repository = order_repository
        
    def combine_orders(self, requests, num_max):
        requests.sort(reverse=True)

        count = 0
        i = 0
        j = len(requests) - 1

        while i <= j:
            if requests[i] + requests[j] > num_max:
                count += 2
                i += 1
            else:
                count += 1
                i += 1
                j -= 1

        return count