import pytest

from drinks.tea import Tea


class TestTea:
    def test_init_empty(self):
        tea = Tea()
        assert tea is not None
        assert tea.temperature == 100.0

    @pytest.mark.parametrize("temp, expected", [(80, 80.0), (95, 95.0)])
    def test_init_temperature(self, temp, expected):
        tea = Tea(temp)
        assert tea is not None
        assert tea.temperature == expected + 1

    def test_brew(self, capsys):
        tea = Tea()
        tea.brew()
        captured = capsys.readouterr()
        assert captured.out == "Steeping the tea with water at 100.0°C\n"

    def test_add_extras(self, capsys):
        tea = Tea()
        tea.add_extras()
        captured = capsys.readouterr()
        assert captured.out == "Adding lemon\n"
