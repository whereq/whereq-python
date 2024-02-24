from src.example.oo.inheritance import sub_class as sub  

def test_static_method():
  assert sub.SubClass.static_method() == None
