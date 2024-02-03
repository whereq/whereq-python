## .\.venv\Scripts\python.exe -m unittest test.BuiltInDataTypesTest

import unittest
import src.base_class as base 

class BaseClassTest(unittest.TestCase):
  def setUp(self):
    self.my_instance = base.BaseClass()

  def test_instanceMethod(self):
    self.my_instance.instance_method()

if __name__ == '__main__':
  unittest.main()