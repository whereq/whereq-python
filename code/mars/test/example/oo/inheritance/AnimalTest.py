import unittest
from src.example.oo.inheritance import Animal

class StringClassTest(unittest.TestCase):
  def test_static_method(self):
    self.animal = Animal.Animal("Cat")

if __name__ == '__main__':
  unittest.main()