from . import base_class
class SubClass(base_class.BaseClass):
  def __init__(self):
    super().__init__()

  @staticmethod
  def static_method():
    # pass  # A static method
    print("A static method in SubClass")