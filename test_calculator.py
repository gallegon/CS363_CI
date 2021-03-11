import pytest
import calculator


class TestCalculator:
	

	def test_add(self):
		assert calculator.add(4,5) == 9

	
	def test_subtract(self):
		assert calculator.subtract(5,3) == 2
