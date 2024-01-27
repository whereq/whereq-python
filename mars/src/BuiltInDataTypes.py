class BuiltInDataTypes:
  """
  This is the class to demonstrate the built-in data types in Python.
  """

  def __init__(self, variable=None):
    self.variable = variable

  def getVariable(self):
    return self.variable

  @classmethod
  def classMethod(cls):
    # pass  # A class method
    print("A class method")

  
  @staticmethod
  def getType(variable):
    return type(variable)

  @staticmethod
  def showAllBuiltInTypes():
    print("\nBuilt-in Data Types\n\nPython has the following data types built-in by default, in these categories:")
    builtInDataTypes = """
      Text Type:      str
      Numeric Types:  int, float, complex
      Sequence Types: list, tuple, range
      Mapping Type:   dict
      Set Types:      set, frozenset
      Boolean Type:   bool
      Binary Types:   bytes, bytearray, memoryview
      None Type:      NoneType
    """

    print(builtInDataTypes + "\n")


if __name__ == "__main__":
  BuiltInDataTypes.showAllBuiltInTypes()
