# __repr__() vs .__str__() 


A Python object has several special methods that provide specific behavior. There are two similar  **special methods**  that describe the object using a string representation. These methods are  `.__repr__()`  and  `.__str__()`. The  `.__repr__()`  method returns a  **detailed description**  for a programmer who needs to maintain and debug the code. The  `.__str__()`  method returns a  **simpler description**  with information for the user of the program.

The  `.__repr__()`  and  `.__str__()`  methods are two of the special methods that you can define for any class. They allow you to control how a program displays an object in several common forms of output, such as what you get from the  `print()`  function, formatted strings, and interactive environments.



## In Short: Use  `.__repr__()`  for Programmers vs  `.__str__()`  for Users
[Python classes](python-classes.md) have a number of [special methods](../articles/python-classes.md/#special-methods-and-protocols). These methods have a **double leading underscore and a double trailing underscore** in their names. You can informally refer to them as dunder methods because of the [double underscores](../articles/python-double-underscore.md) in their names.

-   `.__repr__()`  provides the  **official string representation**  of an object, aimed at the programmer.
-   `.__str__()`  provides the  **informal string representation**  of an object, aimed at the user.



## How Can You Access an Object’s String Representations?
```python
>>> import datetime
>>> today = datetime.datetime.now()

>>> repr(today)
'datetime.datetime(2024, 2, 9, 18, 40, 2, 160890)'
>>> today.__repr__()
'datetime.datetime(2024, 2, 9, 18, 40, 2, 160890)'

>>> str(today)
'2024-02-09 18:40:02.160890'
>>> today.__str__()
'2024-02-09 18:40:02.160890'

>>> format(today)
'2024-02-09 18:40:02.160890'

>>> "{}".format(today)
'2024-02-09 18:40:02.160890'
```

By default, these return the informal string representation of an object which is returned by `.__str__()`.

```python
>>> f"{today}"
'2024-02-09 18:40:02.160890'
```
As was the case with `format()` and `.format()`, f-strings display the informal string representation that `.__str__()` returns. 

```python
>>> f"{today!r}" 
'datetime.datetime(2024, 2, 9, 18, 40, 2, 160890)'
```
The conversion flag `"!r"` overrides the default for f-strings and calls the object’s `.__repr__()` method.

```python
>>> f"{today = }"
'today = datetime.datetime(2024, 2, 9, 18, 40, 2, 160890)'

>>> f"{today = !s}"
'today = 2024-02-09 18:40:02.160890'
```
Use f-strings with an equal sign (`=`) to show both the variable name and its value. 

**NOTE** 
When use an equal sign, the `f-string` defaults to using the official string representation returned by `.__repr__()`.
When use the "!s" conversion, the `f-string` uses the informal string representation.

## Should You Define .__repr__() and .__str__() in a Custom Class?
When define a class, several special methods can be defined to add functionality to the class. More details are in [Object-Oriented Programming (OOP)](../articles/object-oriented-programming.md).

When define a class, it’s a **best practice** to include the official string representation by defining `.__repr__()`. By including this method, the default representation will be avoided, which isn’t very useful in most cases. This method will also provide a fallback option for the informal string representation which can be used for both use cases.

Another best practice is [data classes](../articles/data-classes.md), a default official string representation is already included. You don’t need to define `.__repr__()` yourself unless you want to override the default format.

# Reference
[When Should You Use .__repr__() vs .__str__() in Python?](https://realpython.com/python-repr-vs-str/)

