from src.base_class import BaseClass as Base # Import the BaseClass from the base_class module

class Operator(Base):
  def __init__(self):
    super().__init__()
  
  @staticmethod
  def floor_division(foo, bar): # Also known as integer division
    return foo // bar