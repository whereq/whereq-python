from src.example.oo.inheritance import Animal

class Cat(Animal.Animal):
    def make_sound(self):
        return "Meow!"


cat_instance = Cat("Whiskers")
print(cat_instance.make_sound())  # Output: Meow!