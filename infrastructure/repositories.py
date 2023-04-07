from domain.orders_repositories import Repository
from domain.orders import Order


class OrderRepository(Repository):
    def __init__(self):
        self.orders = []

    def create(self, order: Order) -> str:
        self.orders.append(order)
        return f"Order {order.id} created successfully!"

    def read(self, id: str) -> Order:
        for order in self.orders:
            if order.id == id:
                return order
        raise ValueError(f"Order with id {id} not found!")

    def update(self, order: Order) -> str:
        for i, o in enumerate(self.orders):
            if o.id == order.id:
                self.orders[i] = order
                return f"Order {order.id} updated successfully!"
        raise ValueError(f"Order with id {order.id} not found!")
  
    def delete(self, id: str) -> str:
        for i, order in enumerate(self.orders):
            if order.id == id:
                del self.orders[i]
                return f"Order {id} deleted successfully!"
        raise ValueError(f"Order with id {id} not found!")
    
    def read_all(self) -> list[Order]:
        return self.orders
    
    def read_all_value_of_orders(self) -> list[int]:
        return [order.value for order in self.orders]
