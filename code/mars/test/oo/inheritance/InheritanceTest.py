import unittest
from src.oo.inheritance import StringClass 

class StringClassTest(unittest.TestCase):
  def test_static_method(self):
    StringClass.StringClass.static_method()

if __name__ == '__main__':
  unittest.main()