## .\.venv\Scripts\python.exe -m unittest test.BuiltInDataTypesTest

import src.example.oo.inheritance.base_class as base 

def test_base_class():
  base_instance = base.BaseClass()
  assert base_instance.instance_method() == None
  assert base_instance.class_method() == None
  assert base_instance.static_method() == None