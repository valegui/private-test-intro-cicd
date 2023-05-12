import pytest

from drinks.coffee import Coffee


class TestCoffee:
    def test_init_empty(self):
        coffee = Coffee()
        assert coffee is not None
        assert coffee.temperature == 100.0

    @pytest.mark.parametrize("temp, expected", [(90, 90.0), (100, 100.0)])
    def test_init_temperature(self, temp, expected):
        coffee = Coffee(temp)
        assert coffee is not None
        assert coffee.temperature == expected

    def test_brew(self, capsys):
        coffee = Coffee()
        coffee.brew()
        captured = capsys.readouterr()
        assert captured.out == "Dripping coffee through filter with water at 100.0°C\n"

    def test_add_extras(self, capsys):
        coffee = Coffee()
        coffee.add_extras()
        captured = capsys.readouterr()
        assert captured.out == "Adding sugar and milk\n"
