from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class HotBeverage(ABC):
    temperature: float = 100.0

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour()
        self.add_extras()

    def boil_water(self):
        print("Boiling water")

    def pour(self):
        print("Pour into cup")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass
