from abc import ABC, abstractmethod
from typing import List

from domain.orders import Order


class Repository(ABC):
    
    @abstractmethod
    def create(self, obj: object):
        pass
    
    @abstractmethod
    def read(self, identifier) -> object:
        pass
    
    @abstractmethod
    def update(self, identifier, data: object):
        pass
    
    @abstractmethod
    def delete(self, identifier):
        pass
    
    @abstractmethod
    def read_all(self) -> List[Order]:
        pass
    
    @abstractmethod
    def read_all_value_of_orders(self) -> List[Order]:
        pass
