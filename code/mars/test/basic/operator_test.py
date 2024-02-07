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

    # The difference is due to the floating point precision, 
    # so it's a bad practice to compare floating-point values for exact equality using the == operator.
    self.assertNotEqual(Operator.float_addition(1.1, 2.2), 3.3)
    # The following tests are not equal, but they are almost equal
    self.assertAlmostEqual(Operator.float_addition(1.1, 2.2), 3.3)

  def test_is_close(self):
    self.assertTrue(Operator.is_close(1.1 + 2.2, 3.3)) 
    self.assertTrue(Operator.is_close(1 + 2, 3)) 

  def test_normal_vs_walrus_operator(self):
    nums = [16, 36, 49, 64]
    def normal(x):
      print('The function normal(x) was executed once.')
      return x ** 0.5

    def walrus(x):
      print('The function walrus(x) was executed once.')
      return x ** 0.5

    print('Normal Operator:')
    print([normal(i) for i in nums if normal(i) > 5])

    print('Walrus Operator:')
    print([n for i in nums if (n := walrus(i)) > 5])



if __name__ == '__main__':
  unittest.main()