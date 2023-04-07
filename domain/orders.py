import uuid

class Order:
    def __init__(self, value: int):
        self.id = str(uuid.uuid4())
        self.value = value
