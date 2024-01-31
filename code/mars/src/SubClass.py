from src import BaseClass
class SubClass(BaseClass.BaseClass):
  def __init__(self):
    super().__init__()

  @staticmethod
  def static_method():
    # pass  # A static method
    print("A static method in SubClass")