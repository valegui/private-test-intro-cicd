from dataclasses import dataclass

from .hot_beverage import HotBeverage


@dataclass
class Coffee(HotBeverage):
    def brew(self):
        print("Dripping coffee through filter with water at", f"{self.temperature}°C")

    def add_extras(self):
        print("Adding sugar and milk")
