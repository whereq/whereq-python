from math import isclose
from src.base_class import BaseClass as Base # Import the BaseClass from the base_class module

class Operator(Base):
  def __init__(self):
    super().__init__()
  
  @staticmethod
  def division(foo, bar): # division
    return foo / bar

  @staticmethod
  def floor_division(foo, bar): # Also known as integer division
    return foo // bar
    
  @staticmethod # Check if two values (e.g. float numbers) are almost equal
  def is_close(foo, bar):
    return isclose(foo, bar)

  @staticmethod
  def exponentiation(base, exponent):
    return base ** exponent

  @staticmethod
  def float_addition(foo, bar):
    return foo + bar