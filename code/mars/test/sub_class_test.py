import unittest
from src import sub_class as sub  

class SubClassTest(unittest.TestCase):
  def setUp(self):
    self.obj = sub.SubClass()

  def test_static_method(self):
    sub.SubClass.static_method()

if __name__ == '__main__':
  unittest.main()