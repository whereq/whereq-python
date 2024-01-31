## .\.venv\Scripts\python.exe -m unittest test.BuiltInDataTypesTest

import unittest
from src import BaseClass 

class BaseClassTest(unittest.TestCase):
  def setUp(self):
    self.my_instance = BaseClass.BaseClass()

  def test_instanceMethod(self):
    self.my_instance.instance_method()

if __name__ == '__main__':
  unittest.main()