from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def get_data(self, category: str, search: str = None) -> list:
        pass