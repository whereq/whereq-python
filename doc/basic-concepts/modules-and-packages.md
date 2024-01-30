# Python Modules and Packages

## Table of Contents
* [Python Modules: Overview](#python-modules-overview)
* [The Module Search Path](#the-module-search-path)
* [The import Statement](#the-import-statement)
	* [import <module_name>](#import-module_name)
	* [from <module_name> import <name(s)>](#from-module_name-import-names)
	* [from <module_name> import <name> as <alt_name>](#from-module_name-import-name-as-alt_name)
	* [import <module_name> as <alt_name>](#import-module_name-as-alt_name)
* The dir() Function
* Executing a Module as a Script
* Reloading a Module
* Python Packages
* Package Initialization
* Importing * From a Package
* Subpackages
* Conclusion


## Python Modules: Overview

There are actually three different ways to define a `module` in Python:

 1. A `module` can be written in Python itself. 
 2. A `module` can be written in **C** and loaded dynamically at run-time, like the re ([regular expression](https://realpython.com/regex-python/)) module.  
 3. A **built-in** module is intrinsically contained in the interpreter, like the [itertools module](https://realpython.com/python-itertools/).

A module’s contents are accessed the same way in all three cases: with the import statement.

Here, the focus will mostly be on modules that are written in Python. The cool thing about modules written in Python is that they are exceedingly straightforward to build. All you need to do is create a file that contains legitimate Python code and then give the file a name with a .py extension. That’s it! No special syntax is necessary.

For example, suppose you have created a file called mod.py containing the following:

```python
s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass
```


Several objects are defined in  `mod.py`:

-   `s`  (a string)
-   `a`  (a list)
-   `foo()`  (a function)
-   `Foo`  (a class)

Assuming  `mod.py`  is in an appropriate location, which you will learn more about shortly, these objects can be accessed by  **importing**  the module as follows:

```python 
>>> import mod
>>> print(mod.s)
If Comrade Napoleon says it, it must be right.
>>> mod.a
[100, 200, 300]
>>> mod.foo(['quux', 'corge', 'grault'])
arg = ['quux', 'corge', 'grault']
>>> x = mod.Foo()
>>> x
<mod.Foo object at 0x03C181F0>
```

## The Module Search Path
Continuing with the above example, let’s take a look at what happens when Python executes the statement:
```python
import mod
```

When the interpreter executes the above  `import`  statement, it searches for  `mod.py`  in a  [list](https://realpython.com/python-lists-tuples/)  of directories assembled from the following sources:

-   The directory from which the input script was run or the  **current directory**  if the interpreter is being run interactively
-   The list of directories contained in the  [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)  environment variable, if it is set. (The format for  `PYTHONPATH`  is OS-dependent but should mimic the  [`PATH`](https://realpython.com/add-python-to-path/)  environment variable.)
-   An installation-dependent list of directories configured at the time Python is installed

The resulting search path is accessible in the Python variable  `sys.path`, which is obtained from a module named  `sys`:
```python
>>> import sys
>>> sys.path
['', 'C:\\Users\\john\\Documents\\Python\\doc', 'C:\\Python36\\Lib\\idlelib',
'C:\\Python36\\python36.zip', 'C:\\Python36\\DLLs', 'C:\\Python36\\lib',
'C:\\Python36', 'C:\\Python36\\lib\\site-packages']
```


**Note:**  The exact contents of  `sys.path`  are installation-dependent. The above will almost certainly look slightly different on your computer.

Thus, to ensure your module is found, you need to do one of the following:

-   Put  `mod.py`  in the directory where the input script is located or the  **current directory**, if interactive
-   Modify the  `PYTHONPATH`  environment variable to contain the directory where  `mod.py`  is located before starting the interpreter
    -   **Or:**  Put  `mod.py`  in one of the directories already contained in the  `PYTHONPATH`  variable
-   Put  `mod.py`  in one of the installation-dependent directories, which you may or may not have write-access to, depending on the OS

There is actually one additional option: you can put the module file in any directory of your choice and then modify  `sys.path`  at run-time so that it contains that directory. For example, in this case, you could put  `mod.py`  in directory  `C:\Users\john`  and then issue the following statements:

```python
>>> sys.path.append(r'C:\Users\john')
>>> sys.path
['', 'C:\\Users\\john\\Documents\\Python\\doc', 'C:\\Python36\\Lib\\idlelib',
'C:\\Python36\\python36.zip', 'C:\\Python36\\DLLs', 'C:\\Python36\\lib',
'C:\\Python36', 'C:\\Python36\\lib\\site-packages', 'C:\\Users\\john']
>>> import mod
```


Once a module has been imported, you can determine the location where it was found with the module’s `__file__` attribute:
```python
>>> import mod
>>> mod.__file__
'C:\\Users\\john\\mod.py'

>>> import re
>>> re.__file__
'C:\\Python36\\lib\\re.py'
```

The directory portion of `__file__` should be one of the directories in `sys.path`.

## The import Statement
**Module**  contents are made available to the caller with the  `import`  statement. The  `import`  statement takes many different forms, shown below.

### import <module_name>

The simplest form is the one already shown above:

```python
import <module_name>
```


Note that this  _does not_  make the module contents  _directly_  accessible to the caller. Each module has its own  **private symbol table**, which serves as the global symbol table for all objects defined  _in the module_. Thus, a module creates a separate  **namespace**, as already noted.

The statement  `import <module_name>`  only places  `<module_name>`  in the caller’s symbol table. The  _objects_  that are defined in the module  _remain in the module’s private symbol table_.

From the caller, objects in the module are only accessible when prefixed with  `<module_name>`  via  **dot notation**, as illustrated below.

After the following  `import`  statement,  `mod`  is placed into the local symbol table. Thus,  `mod`  has meaning in the caller’s local context:

```python
>>> import mod
>>> mod
<module 'mod' from 'C:\\Users\\john\\Documents\\Python\\doc\\mod.py'>
```

But `s` and `foo` remain in the module’s private symbol table and are not meaningful in the local context:
```python
>>> s
NameError: name 's' is not defined
>>> foo('quux')
NameError: name 'foo' is not defined
```

To be accessed in the local context, names of objects defined in the module must be prefixed by `mod`:
```python
>>> mod.s
'If Comrade Napoleon says it, it must be right.'
>>> mod.foo('quux')
arg = quux
```

Several comma-separated modules may be specified in a single import statement:
```python
import <module_name>[, <module_name> ...]
```

### from <module_name> import <name(s)>
An alternate form of the `import` statement allows individual objects from the module to be imported _directly into the caller’s symbol table_:

```python
from <module_name> import <name(s)>
```

Following execution of the above statement, `<name(s)>` can be referenced in the caller’s environment without the `<module_name>` prefix:

```python
>>> from mod import s, foo
>>> s
'If Comrade Napoleon says it, it must be right.'
>>> foo('quux')
arg = quux

>>> from mod import Foo
>>> x = Foo()
>>> x
<mod.Foo object at 0x02E3AD50>
```

Because this form of `import` places the object names directly into the caller’s symbol table, any objects that already exist with the same name will be _overwritten_:

```python
>>> a = ['foo', 'bar', 'baz']
>>> a
['foo', 'bar', 'baz']

>>> from mod import a
>>> a
[100, 200, 300]
```

It is even possible to indiscriminately `import` everything from a module at one fell swoop:

```python
from <module_name> import *
```

This will place the names of _all_ objects from `<module_name>` into the local symbol table, with the exception of any that begin with the [underscore (`_`) character](https://realpython.com/python-double-underscore/).

```python
>>> from mod import *
>>> s
'If Comrade Napoleon says it, it must be right.'
>>> a
[100, 200, 300]
>>> foo
<function foo at 0x03B449C0>
>>> Foo
<class 'mod.Foo'>
```

This isn’t necessarily recommended in large-scale production code. It’s a bit dangerous because you are entering names into the local symbol table _en masse_. Unless you know them all well and can be confident there won’t be a conflict, you have a decent chance of overwriting an existing name inadvertently. However, this syntax is quite handy when you are just mucking around with the interactive interpreter, for testing or discovery purposes, because it quickly gives you access to everything a module has to offer without a lot of typing.

### from <module_name> import <name> as <alt_name>
It is also possible to `import` individual objects but enter them into the local symbol table with alternate names:

```python
from <module_name> import <name> as <alt_name>[, <name> as <alt_name> …]
```

This makes it possible to place names directly into the local symbol table but avoid conflicts with previously existing names:

```python
>>> s = 'foo'
>>> a = ['foo', 'bar', 'baz']

>>> from mod import s as string, a as alist
>>> s
'foo'
>>> string
'If Comrade Napoleon says it, it must be right.'
>>> a
['foo', 'bar', 'baz']
>>> alist
[100, 200, 300]
```

### import <module_name> as <alt_name>
You can also import an entire module under an alternate name:
```python
import <module_name> as <alt_name>
```
```python
>>> import mod as my_module
>>> my_module.a
[100, 200, 300]
>>> my_module.foo('qux')
arg = qux
```
Module contents can be imported from within a [function definition](https://realpython.com/defining-your-own-python-function/). In that case, the `import` does not occur until the function is _called_:
```python
>>> def bar():
...     from mod import foo
...     foo('corge')
...

>>> bar()
arg = corge
```

However, **Python 3** does not allow the indiscriminate `import *` syntax from within a function:
```python
>>> def bar():
...     from mod import *
...
SyntaxError: import * only allowed at module level
```

Lastly, a [`try`  statement with an  `except ImportError`](https://realpython.com/python-exceptions/) clause can be used to guard against unsuccessful `import` attempts:
```python
>>> try:
...     # Non-existent module
...     import baz
... except ImportError:
...     print('Module not found')
...

Module not found
```

```python
>>> try:
...     # Existing module, but non-existent object
...     from mod import baz
... except ImportError:
...     print('Object not found in module')
...

Object not found in module
```
# References
[Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)