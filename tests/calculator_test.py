"""Testing the Calculator"""
from calculator import Calculator, Operation
def test_calculator_is_instance():
    calculator = Calculator()
    assert isinstance(calculator, Calculator)
    
def test_calculator_result_property():
    calc1 = Calculator()
    calc2 = Calculator()
    calc1.result = 5
    calc2.result = 6
    assert calc1.result == 5
    assert calc2.result == 6

def test_calculator_add_method():
    calculator = Calculator()
    assert calculator.add(3,4) == 7
    assert calculator.add(2,3) == 5
    assert calculator.add(2,3,4,5) == 14

def test_calculator_sub_method():
    calculator = Calculator()
    assert calculator.sub(3,2) == 1
    assert calculator.sub(2,6) == -4

def test_calculator_mul_method():
    calculator = Calculator()
    assert calculator.mul(3,4) == 12
    assert calculator.mul(9,0) == 0

def test_calculator_div_method():
    calculator = Calculator()
    assert calculator.div(3,0) == "It is impossible to divide by 0"
    assert calculator.div(9,3) == 3
