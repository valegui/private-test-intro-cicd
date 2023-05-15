from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class HotBeverage(ABC):
    """Abstract class to prepare hot beverages

    Attributes
    ----------
    temperature : float
        Temperature at which the hot beverage is prepared.
    """

    temperature: float = 100.0

    def prepare_recipe(self):
        """Prepares the hot beverage"""
        self.boil_water()
        self.brew()
        self.pour()
        self.add_extras()

    def boil_water(self):
        """Boils water"""
        print("Boiling water")

    def pour(self):
        """Pours beverage into cup"""
        print("Pour into cup")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass
