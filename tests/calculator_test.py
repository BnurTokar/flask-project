"""Testing the Calculator"""


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

from calculator import Calculator

def test_calculator_add_method():
    """arranging step"""
    value_1 = 3
    value_2 = 4
    calculator = Calculator()
    """acting step"""
    result= calculator.add(value_1, value_2)
    """assertion step"""
    assert result == 7

def test_calculator_sub_method():
    """arranging step"""
    value_1 = 3
    value_2 = 2
    calculator = Calculator()
    """acting and assertion steps"""
    assert calculator.sub(3,2) == 1

def test_calculator_mul_method():
    calculator = Calculator()
    assert calculator.mul(3,4) == 12
    assert calculator.mul(9,0) == 0

def test_calculator_div_method():
    calculator = Calculator()
    assert calculator.div(3,0) == "It is impossible to divide by 0"
    assert calculator.div(9,3) == 3
