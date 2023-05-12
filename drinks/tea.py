from dataclasses import dataclass

from .hot_beverage import HotBeverage


@dataclass
class Tea(HotBeverage):
    def brew(self):
        print("Steeping the tea with water at", f"{self.temperature}°C")

    def add_extras(self):
        print("Adding lemon")
