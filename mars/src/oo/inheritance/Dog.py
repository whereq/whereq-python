from src import Animal

class Dog(Animal.Animal):
    def make_sound(self):
        return "Woof!"


dog_instance = Dog("Buddy")
print(dog_instance.name)  # Output: Buddy

# Calling methods from the subclasses
print(dog_instance.make_sound())  # Output: Woof!