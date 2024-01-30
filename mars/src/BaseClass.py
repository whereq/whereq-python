class BaseClass:
  def __init__(self):
    # pass  # Constructor method
    print("A constructor method")

  def instance_method(self):
    # pass  # An instance method
    print("A instance method")

  @classmethod
  def class_method(cls):
    # pass  # A class method
    print("A class method")

  @staticmethod
  def static_method():
    # pass  # A static method
    print("A static method")

if __name__ == "__main__":
  # Create an instance of MyClass
  my_instance = BaseClass()

  # Call the instance method
  my_instance.instance_method()

  # Call the class method
  BaseClass.class_method()

  # Call the static method
  BaseClass.static_method()