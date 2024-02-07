import unittest
from src.example.basic import operator # Import the Operator class from the operator module

class OperatorTest(unittest.TestCase):
  def test_floor_division(self):
    self.assertEqual(operator.Operator.floor_division(5, 2), 2)

if __name__ == '__main__':
  unittest.main()