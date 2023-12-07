import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_multiply(self):
        assert self.calc.multiply(self, 3, 2) == 6
    def test_division(self):
        assert self.calc.division(self, 20, 5) == 4
    def test_subtraction(self):
        assert self.calc.subtraction(self, 18, 2) == 16
    def test_adding(self):
        assert self.calc.adding(self, 5, 5) == 10
    def test_exponentiation(self):
        assert self.calc.exponentiation(self, 3, 3) == 27
    def teardown(self):
        print('Выполнение метода Teardown')
