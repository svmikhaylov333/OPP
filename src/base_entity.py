from abc import ABC, abstractmethod


class BaseStoreEntity(ABC):
    pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def total_price(self) -> float:
        pass

    @abstractmethod
    def get_product_count(self) -> int:
        pass
