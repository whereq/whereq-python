class BaseClass:
  def __init__(self):
    # pass  # Constructor method
    print("A constructor method")

  def instanceMethod(self):
    # pass  # An instance method
    print("A instance method")

  @classmethod
  def classMethod(cls):
    # pass  # A class method
    print("A class method")

  @staticmethod
  def staticMethod():
    # pass  # A static method
    print("A static method")

if __name__ == "__main__":
  # Create an instance of MyClass
  my_instance = BaseClass()

  # Call the instance method
  my_instance.instanceMethod()

  # Call the class method
  BaseClass.classMethod()

  # Call the static method
  BaseClass.staticMethod()