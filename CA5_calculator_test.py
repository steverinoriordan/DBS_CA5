import unittest
import math


c = [8,2,2]
d = [9,16]
e = [6,5,4]
f = [-6,-10,-2]
reduce(lambda x, y: x+y, c)
reduce(lambda x, y: x-y, c)
reduce(lambda x, y: x*y, c)
reduce(lambda x, y: x/y, c)
reduce(lambda x, y: x**y, c)
map(lambda x:math.sqrt(x), d)
map(lambda x:x*x, c)
map(lambda x:x*x*x, c)
map(lambda x:math.factorial(x), c)
map(lambda x:abs(x), f)



    # test the calculator functionality
class TestCalculator(unittest.TestCase):

    # this tests the addition functionality for a list of numbers
    # 8 + 2 + 2 = 12
    def test_calculator_add_method_returns_correct_result(self):
        result = reduce(lambda x, y: x+y, c)
        self.assertEqual(12.0, result)
        
    # this tests the subtraction functionality for a list of numbers
    # 8 - 2 - 2 = 4
    def test_calculator_subtract_method_returns_correct_result(self):
        result = reduce(lambda x, y: x-y, c)
        self.assertEqual(4.0, result)
        
    # this tests the multiplication functionality for a list of numbers
    # 8 * 2 * 2 = 32
    def test_calculator_multiply_method_returns_correct_result(self):
        result = reduce(lambda x, y: x*y, c)
        self.assertEqual(32.0, result)
        
    # this tests the division functionality for a list of numbers
    # 8 / 2 / 2 = 2
    def test_calculator_divide_method_returns_correct_result(self):
        result = reduce(lambda x, y: x/y, c)
        self.assertEqual(2.0, result)
        
    # this tests the exponent functionality for a list of numbers
    # 8**2**2 = 8
    def test_calculator_exponent_method_returns_correct_result(self):
        result = reduce(lambda x, y: x**y, c)
        self.assertEqual(4096.0, result)
        
    # this tests the square root functionality for a list of numbers
    # sq root of 9 = 3 and sq root of 16 = 4
    def test_calculator_square_root_method_returns_correct_result(self):
        result = map(lambda x:math.sqrt(x), d)
        self.assertEqual([3.0,4.0], result)
        
    # this tests the squared functionality for a list of numbers
    # 8 squared = 64, 2 squared = 4, 2 squared = 4, 
    def test_calculator_squared_method_returns_correct_result(self):
        result = map(lambda x:x*x, c)
        self.assertEqual([64.0,4.0,4.0], result)
        
    # this tests the cubed functionality for a list of numbers
    # 8 cubed = 512, 2 cubed = 8, 2 cubed = 8, 
    def test_calculator_cubed_method_returns_correct_result(self):
        result = map(lambda x:x*x*x, c)
        self.assertEqual([512.0,8.0,8.0], result)
        
    # this tests the factorial functionality for a list of numbers
    # 6 factorial = 720, 5 factorial = 120, 4 factorial = 24, 
    def test_calculator_factorial_method_returns_correct_result(self):
        result = map(lambda x:math.factorial(x), e)
        self.assertEqual([720.0,120.0,24.0], result)
        
    # this tests the absolute value functionality for a list of numbers
    # absolute value of -6 = 6, absolute value of -10 = 10, absolute value of -2 = 2 
    def test_calculator_absolute_value_method_returns_correct_result(self):
        result = map(lambda x:abs(x), f)
        self.assertEqual([6.0,10.0,2.0], result)
        
if __name__ == '__main__':
    unittest.main()