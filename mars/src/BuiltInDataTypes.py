class BuiltInDataTypes:
  """
  This is the class to demonstrate the built-in data types in Python.
  """

  def __init__(self, variable=None):
    self.variable = variable

  def get_variable(self):
    return self.variable

  @classmethod
  def class_method(cls):
    # pass  # A class method
    print("A class method")

  
  @staticmethod
  def get_type(variable):
    return type(variable)

  @staticmethod
  def show_all_built_in_types():
    print("\nBuilt-in Data Types\n\nPython has the following data types built-in by default, in these categories:")
    built_in_data_types = """
      Text Type:      str
      Numeric Types:  int, float, complex
      Sequence Types: list, tuple, range
      Mapping Type:   dict
      Set Types:      set, frozenset
      Boolean Type:   bool
      Binary Types:   bytes, bytearray, memoryview
      None Type:      NoneType
    """

    print(built_in_data_types + "\n")


if __name__ == "__main__":
  BuiltInDataTypes.show_all_built_in_types()
