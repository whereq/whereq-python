## .\.venv\Scripts\python.exe -m unittest test.BuiltInDataTypesTest

import unittest
from src import built_in_data_types as bdt

class BuiltInDataTypesTest(unittest.TestCase):
  def setUp(self):
    self.my_instance = bdt.BuiltInDataTypes(77)

  def test_get_variable(self):
    result = self.my_instance.get_variable()
    self.assertIsNotNone(result)  

  def test_get_type(self):
    theType = bdt.BuiltInDataTypes.get_type(37)
    print(f'Type of 37 is {theType}')
    print(int.__class__)
    self.assertEqual(theType, type(37))

    theType = bdt.BuiltInDataTypes.get_type("Hello, Mars!")
    print(f'Type of "Hello, Mars!" is {theType}')
    self.assertEqual(theType, type("Hello, Mars!"))

if __name__ == '__main__':
  unittest.main()