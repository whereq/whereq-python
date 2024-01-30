## .\.venv\Scripts\python.exe -m unittest test.BuiltInDataTypesTest

import unittest
from src import BuiltInDataTypes

class BuiltInDataTypesTest(unittest.TestCase):
  def setUp(self):
    self.my_instance = BuiltInDataTypes.BuiltInDataTypes(77)

  def test_get_variable(self):
    result = self.my_instance.get_variable()
    self.assertIsNotNone(result)  

  def test_get_type(self):
    theType = BuiltInDataTypes.BuiltInDataTypes.get_type(37)
    print(f'Type of 37 is {theType}')
    print(int.__class__)
    self.assertEqual(theType, type(37))

    theType = BuiltInDataTypes.BuiltInDataTypes.get_type("Hello, Mars!")
    print(f'Type of "Hello, Mars!" is {theType}')
    self.assertEqual(theType, type("Hello, Mars!"))

if __name__ == '__main__':
  unittest.main()