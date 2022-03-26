""" This is the Calculator Class"""
from operations import Operation, Addition as Add, Subtraction as Sub, Multiplication as Mul, Division as Div, Addition
from calculation import Calculation

class Calculator:
    """This is Calculator class"""
    @staticmethod
    def add (*arg):#arg gets unlimited value for add operation
        "This is add operation"
        result = 0
        for value in arg:
            calculation = Calculation(result, value)
            calculation.setStrategy(Add) #calling operations.Addition() class
            result =+ calculation.get_result()
        return result

    @staticmethod
    def sub(value_1,value_2):
        calculation = Calculation(value_1, value_2 )
        calculation.setStrategy(Sub) #calling operations.Subtraction() class
        return calculation.get_result()

    @staticmethod
    def mul(value_1, value_2):
        calculation = Calculation(value_1, value_2)
        calculation.setStrategy(Mul) #calling operations.Multiplication() class
        return calculation.get_result()

    @staticmethod
    def div(value_1, value_2):
        calculation = Calculation(value_1, value_2)
        calculation.setStrategy(Div) #calling operations.Division() class
        return calculation.get_result()

