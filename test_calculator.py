import calculator


class TestCalculator:

    def test_add(self):
        assert calculator.add(4, 5) == 9

    def test_subtract(self):
        assert calculator.subtract(5, 3) == 2

    def test_multiply(self):
        assert calculator.multiply(20, 5) == 100
