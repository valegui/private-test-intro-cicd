from dataclasses import dataclass

from .hot_beverage import HotBeverage


@dataclass
class Coffee(HotBeverage):
    """Class to prepare coffee

    See Also
    --------
    HotBeverage
    """

    def brew(self):
        """Drips coffee with water at `temperature`"""
        print("Dripping coffee through filter with water at", f"{self.temperature}°C")

    def add_extras(self):
        """Add sugar and milk"""
        print("Adding sugar and milk")
