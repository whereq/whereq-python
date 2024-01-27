# import VS from ... import

## 1. Introduction
In Python code, you can import modules or objects from modules. There are mainly two ways to import: `import <module_name>` and `from <module_name> import <name(s)>`. This article primarily compares the two. To illustrate, a module named `test` is defined for later testing. The content of the `ModuleTest.py` file is as follows:

```python
theArray = [1, 2, 3]
theStr = 'abc'

class ModuleTest():
    def __init__(self):
        self.desc = 'ModuleTest'

    def printDesc(self):
        print(self.desc)

```

## 2. Comparison of Two Ways
### 2.1 import <module_name>
One of the commands for importing Python modules is `import <module_name>`. After executing the `import <module_name>` command, the Python execution process is as follows:

1. First, it looks for `module_name` in sys.modules, which contains a cache of all previously imported modules.
2. If `module_name` is not found in the module cache, Python continues to search the list of built-in modules, which are modules pre-installed with Python and can be found in the Python standard library.
3. If it is still not found, Python searches in the directory list defined by sys.path. This list usually includes the current directory and searches it first.
4. If `module_name` is found, it binds it to the local namespace for later use. If not found, it raises a ModuleNotFoundError.

Note: After importing the module, you can use the module's `__file__` attribute to get the directory where the module is located, which is one of the directories in sys.path. sys.path[0] is empty, representing the current directory. An example is as follows:

```python
>>> import test.ModuleTest
>>> test.ModuleTest.__file__
'[absolute_path]\\mars\\test\\ModuleTest.py'
>>> import re
>>> re.__file__
'[absolute_path]\\Python-3.12.1\\Lib\\re\\__init__.py'
>>> import sys
>>> sys.path
['', '[absolute_path]\\Python-3.12.1\\python312.zip', '[absolute_path]\\Python-3.12.1\\DLLs', '[absolute_path]\\Python-3.12.1\\Lib', '[absolute_path]\\Python-3.12.1', '[absolute_path]\\Python-3.12.1\\Lib\\site-packages']
>>> import os
>>> os.getcwd()
'[absolute_path]\\mars'
>>> import mod
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'mod'
```

After importing `<module_name>`, you cannot directly access the contents of the module. Each module has its private symbol table, which is the global symbol table for all objects defined in the module, creating a separate namespace for the module. After executing `import <module_name>`, `<module_name>` is placed in the local symbol table of the caller, but the objects defined in the module remain in the module's private symbol table. Accessing objects defined in the module requires using the dot (.) symbol. An example is as follows:

```python
>>> import test.ModuleTest
>>> module
<module 'test.ModuleTest' from '[absolute_path]\\mars\\test\\ModuleTest.py'>
>>> theArray
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'theArray' is not defined
>>> theStr
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'theStr' is not defined
>>> test.ModuleTest.theArray
[1, 2, 3]
>>> test.ModuleTest.theStr
'abc'

```

When importing a module, sometimes the module name is very long, making it inconvenient to access the module's contents each time. Therefore, you can use the `import ... as ...` syntax to rename the module for ease of use. The example code is as follows:

```python
>>> import test.ModuleTest as tmt
>>> test.ModuleTest
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'test' is not defined
>>> tmt
<module 'test.ModuleTest' from '[absolute_path]\\mars\\test\\ModuleTest.py'>
>>> test.ModuleTest.theArray
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'test' is not defined
>>> tmt.theArray
[1, 2, 3]

```

### 2.2 from <module_name> import <name(s)>
The `from <module_name> import <name(s)>` command can directly import objects from a module. After the command is executed, the objects from the module are referenced in the caller's environment and can be directly accessed without adding the module prefix. This method of import adds the objects from the module directly to the caller's symbol table and will override any same-named objects in the caller's symbol table.

```python
>>> theArray = [1, 2]
>>> theArray
[1, 2]
>>> from test.ModuleTest import theArray
>>> theArray
[1, 2, 3]
>>> from test.ModuleTest import theInt
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'theInt' from 'test.ModuleTest' ([absolute_path]\mars\test\ModuleTest.py)
>>> from test.ModuleTest import theStr
>>> theStr
'abc'
>>> test.ModuleTest
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'test' is not defined
>>> from test.ModuleTest import ModuleTest
>>> mt = ModuleTest()
>>> mt.printDesc()
ModuleTest
```

To address the issue of long import names, you can also use `from ... import ... as ...` to rename the imported objects. This approach can also be used to resolve naming conflicts introduced by importing objects.

### 2.3 from <module_name> import *
The `from <module_name> import *` command can indiscriminately import most objects from the module (excluding those starting with an underscore). This approach carries a higher risk and makes code reading less straightforward. Therefore, it is not detailed here, and this usage is not recommended.


### 2.4 dir()
The built-in function `dir()` in Python returns a list of names defined in the namespace. Using `dir()`, you can observe changes in the local symbol table before and after import statements, as well as inspect objects defined in a module. Here's an example:
```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> theArray = [1, 2]
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'theArray']
>>> import test
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'test', 'theArray']
>>> from test.ModuleTest import theStr
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'test', 'theArray', 'theStr']
>>> import test.ModuleTest
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'test', 'theArray', 'theStr']
>>> from test import ModuleTest as mt
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'mt', 'test', 'theArray', 'theStr']
>>> mt.theArray
[1, 2, 3]
>>> dir(test)
['ModuleTest', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
>>> dir(test.ModuleTest)
['ModuleTest', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'theArray', 'theStr']
>>> dir(mt)
['ModuleTest', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'theArray', 'theStr']
```