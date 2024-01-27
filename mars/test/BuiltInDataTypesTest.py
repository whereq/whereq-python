# .\.venv\Scripts\python.exe -m unittest test.BuiltInDataTypesTest

import unittest
from src import BuiltInDataTypes as BuiltInDataTypes

class TestMyClass(unittest.TestCase):
  def setUp(self):
    self.my_instance = BuiltInDataTypes.BuiltInDataTypes(77)

  def test_getVariable(self):
    result = self.my_instance.getVariable()
    self.assertIsNotNone(result)  

  def test_getType(self):
      theType = BuiltInDataTypes.BuiltInDataTypes.getType(37)
      print(f'Type of 37 is {theType}')
      print(int.__class__)
      self.assertEqual(theType, type(37))

      theType = BuiltInDataTypes.BuiltInDataTypes.getType("Hello, Mars!")
      print(f'Type of "Hello, Mars!" is {theType}')
      self.assertEqual(theType, type("Hello, Mars!"))

if __name__ == '__main__':
  unittest.main()