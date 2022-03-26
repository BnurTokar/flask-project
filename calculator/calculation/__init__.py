""" This is the Calculation Class"""
from calculator.operations import Operation


class Calculation:
    """ This class is for get_result operation"""
    """"Strategy Pattern"""

    opr = Operation

    def __init__(self,value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def setStrategy(self, opr = None):
        """opr interface created from Operation class"""
        self.opr = opr

    def get_result(self):
        return self.opr.get_result(self.value_1, self.value_2)

