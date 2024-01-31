import unittest
from src import SubClass  

class SubClassTest(unittest.TestCase):
  def setUp(self):
    self.obj = SubClass.SubClass()

  def test_static_method(self):
    SubClass.SubClass.static_method()

if __name__ == '__main__':
  unittest.main()