import unittest
from src.example.oo.inheritance import Animal, Dog, Cat

class AnimalTest(unittest.TestCase):
  def test_dog(self):
    dog_instance = Dog.Dog("Wang")
    self.assertEqual("Wang", dog_instance.name)  
    self.assertEqual("Woof!", dog_instance.make_sound())  

  def test_cat(self):
    cat_instance = Cat.Cat("Mao")
    self.assertEqual("Mao", cat_instance.name)  
    self.assertEqual("Meow!", cat_instance.make_sound())  


if __name__ == '__main__':
  unittest.main()