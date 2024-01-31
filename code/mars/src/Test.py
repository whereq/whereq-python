# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

# Subclass inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Subclass inheriting from Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating instances of the subclasses
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")

# Accessing attributes from the base class
print(dog_instance.name)  # Output: Buddy

# Calling methods from the subclasses
print(dog_instance.make_sound())  # Output: Woof!
print(cat_instance.make_sound())  # Output: Meow!
