class Operation():
    """This is Operation class"""
    def get_result(self):
        pass

class Addition(Operation):
    "This is Addition class"
    @staticmethod
    def get_result(value_1, value_2):
        """ This is the add method"""
        return value_1 + value_2

class Subtraction(Operation):
    "This is Subtraction class"
    @staticmethod
    def get_result(value_1, value_2):
        """ This is the sub method"""
        return value_1 - value_2

class Multiplication(Operation):
    "This is Multiplication class"
    @staticmethod
    def get_result(value_1, value_2):
        """ This is the mul method"""
        return value_1 * value_2

class Division(Operation):
    "This is Division class"
    @staticmethod
    def get_result(value_1, value_2):
        """ This is the div method"""
        try:
            return value_1 / value_2
        except ZeroDivisionError:
            return "It is impossible to divide by 0"

