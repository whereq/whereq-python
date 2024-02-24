from src.types.string import string_class

def test_static_method():
  assert string_class.StringClass.static_method() == None
