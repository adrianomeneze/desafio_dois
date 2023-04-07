from domain.orders import Order
from domain.orders_repositories import Repository
from infrastructure.repositories import OrderRepository
from application.orders import Orders


class Main:
    if __name__ == '__main__':
        try:
            num_max = 100
            expected_orders = 2

            order_repository  = OrderRepository()
            order1 = Order(70)
            order_repository.create(order1)

            order2 = Order(30)
            order_repository.create(order2)

            order3 = Order(10)
            order_repository.create(order3)
            
            orders = order_repository.read_all_value_of_orders()
            print(f"List of values ​​of registered requests: {orders}")     
            
            orders_obj = Orders(order_repository)

            how_many = orders_obj.combine_orders(orders, num_max)
            assert how_many == expected_orders
            print("Successfully!!")
        except Exception as e:
            print("An error occurred:", e)
main = Main()

