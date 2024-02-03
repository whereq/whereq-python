import unittest
from src.types.string import string_class

class StringClassTest(unittest.TestCase):
  def test_static_method(self):
    string_class.StringClass.static_method()

if __name__ == '__main__':
  unittest.main()