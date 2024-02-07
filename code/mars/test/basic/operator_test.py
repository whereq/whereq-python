import unittest
from src.example.basic.operator import Operator # Import the Operator class from the operator module

class OperatorTest(unittest.TestCase):

  def test_division(self):
    self.assertEqual(Operator.division(5, 2), 2.5)
    self.assertEqual(Operator.division(6, 2), 3.0)
    self.assertEqual(Operator.division(10, 5j), -2j)

  def test_floor_division(self):
    self.assertEqual(Operator.floor_division(5, 2), 2)
    self.assertEqual(Operator.floor_division(10, -4), -3)

  def test_exponentiation(self):
    self.assertEqual(Operator.exponentiation(2, 3), 8)

  def test_float_addition(self):
    self.assertEqual(Operator.float_addition(2.5, 3.5), 6.0)

if __name__ == '__main__':
  unittest.main()