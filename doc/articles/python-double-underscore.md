# Single and Double Underscores in Python Names

Python doesn’t have the notion of public and private members. It has neither dedicated [keywords](python-keywords.md) nor syntax for defining them. So, you can always access the members of a Python class.

Python doesn’t use the terms public and private. Instead, it uses the terms **public** and **non-public**.

In Python, if a name starts with a letter in uppercase or lowercase, then you should consider that name **public** and, therefore, part of the code’s API. In contrast, if a name starts with an underscore character (`_`), then you should consider that name **non-public**, meaning it’s not a part of the code’s API.

The Python community uses the underscore character (`_`) as part of other naming conventions. Here’s a summary of what [PEP 8](https://peps.python.org/pep-0008/) says about using this character in names:


|Convention  |Example  |Meaning  |
|--|--|--|
|Single leading underscore  |_variable  |Indicates that the name is meant for internal use only  |
|Single trailing underscore  |class_  |Avoids naming conflicts with Python keywords and built-in names  |
|Double leading underscore  |__attribute  |Triggers name mangling in the context of Python classes  |
|Double leading and trailing underscore  |__name__  |Indicates special attributes and methods that Python provides  |
|Single underscore  |_  |Indicates a temporary or throwaway variable  |

Note that only two of these conventions enforce specific Python behaviors. Using double leading underscores triggers [name mangling](python-pep8.md/#naming-conventions) in Python classes. You’ll learn more about this behavior in the section on [name mangling](python-double-underscore/#double-leading-underscore-in-classes-pythons-name-mangling).

Additionally, those names with double leading and trailing underscores that are listed in the Python  [data model](https://docs.python.org/3/reference/datamodel.html)  trigger internal behaviors in specific contexts. You’ll also learn more about this topic in the section on  [dunder names in Python](python-double-underscore.md/#dunder-names-in-python).

**Note:**  Python gives special treatment to the single underscore (`_`), but only within  `match`  …  `case`  statements. You’ll learn more about this  [later](python-double-underscore.md/#other-usages-of-underscores-in-python).

## Single Leading Underscore in Python Names

Python doesn’t have dedicated keywords and syntax to make objects public or private. Therefore, Python calls its objects **public** or **non-public** and doesn’t restrict access to them.

## Public and Non-Public Names in Modules and Packages

Python modules might be one of those places where you’ll need to decide which names should be public and which should be non-public. At the module level, you can have some of the following objects:

-   [Constants](python-constants.md)
-   [Variables](python-variables.md)
-   [Functions](define-python-function.md)
-   [Classes](python-classes.md)

You may need to allow your users to access these objects as part of your module’s API. However, in some cases, you may need to communicate that some of your module-level objects aren’t intended to be part of the API.

Some common examples of module-level non-public objects include:

-   Internal variables and constants
-   Helper functions and classes

In the following sections, you’ll learn about these types of objects. You’ll also learn about non-public modules. Yes, you can even have non-public modules in your packages.

### Internal Variables and Constants
```python
_count = 0

def increment():
    global _count
    _count += 1

def decrement():
    global _count
    _count -= 1

def get_count():
    return _count
```
In the above example, the `module` employs a `global variable` named **_count** to maintain a counter, alongside `public` functions for **incrementing**, **decrementing**, and **retrieving the count's state**. While these functions are accessible to users, the **_count** variable remains `non-public`, indicated by the `leading underscore` in its name. This convention signals to users that they should not manipulate **_count** directly in their code. By adhering to this guideline, users can avoid potential invalid states in the counting process. Instead, they should interact with the module through the provided mutator functions **increment()** and **decrement()** for modifying the count and use **get_count()** to retrieve its value when necessary.

```python
_PI = 3.14

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(_PI * self.radius**2, 2)
```
The above example shows another situation where you’d like to make your objects non-public is when you have a constant that’s only relevant to the internal working of its containing module. 


## Wildcard Imports and Non-Public Names
**NOTE**: `Wildcard Imports` don’t import non-public names!!!

**E.g. shape.py

```python
_PI = 3.14

class Circle:
    def __init__(self, radius):
        self.radius = _validate(radius)

    def calculate_area(self):
        return round(_PI * self.radius**2, 2)

class Square:
    def __init__(self, side):
        self.side = _validate(side)

    def calculate_area(self):
        return round(self.side**2, 2)

def _validate(value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        return value
```


```python
>>> from shapes import *

>>> dir()
[
    'Circle',
    'Square',
    ...
]

```
In the above code snippet, Wildcard Import only imports the `Circle` and `Square` classes. The `_PI` constant and the `_validate()` function aren’t in the current [namespace](python-namespace-package.md).


Python enforces the above behavior. However, this behavior only applies to wildcard imports, any `non-public` names can still be imported by using other import statement forms like below：
```python
>>> from shapes import _PI

>>> _PI
3.14

>>> import shapes

>>> shapes._PI
3.14
```

## Class With Non-Public Members

```python
# point.py
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = _validate(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = _validate(value)

def _validate(value):
    if not isinstance(value, int | float):
        raise ValueError("number expected")
    return value
```

```python
>>> from point import Point

>>> point = Point(12, 5)

>>> point.x
12
>>> point.y
5

>>> point.x = 24
>>> point.x
24

>>> point.y = "10"
Traceback (most recent call last):
    ...
ValueError: number expected
```

In the above example, when you try to assign an invalid value to one of the coordinates, you get a `ValueError`. This happens because the setter method of a property runs whenever you assign a new value. So, the `_validate()` function runs every time you try to update the value of `.x` or `.y`.



### Understanding Name Mangling

When you name an attribute or method using two leading underscores, Python automatically renames it by prefixing its name with the class name and a single leading underscore. This renaming process is known as  **name mangling**.

The following sample class shows how this happens:

```python
`>>> class SampleClass:
...     def __init__(self, attribute):
...         self.__attribute = attribute
...     def __method(self):
...         print(self.__attribute)
...

>>> sample_instance = SampleClass("Hello!")
>>> vars(sample_instance)
{'_SampleClass__attribute': 'Hello!'}
```
In this class,  `.__attribute`  and  `.__method()`  have two leading underscores in their names. Python mangles those names to  `._SampleClass__attribute`  and  `._SampleClass__method()`, respectively. Python has automatically added the prefix  `_SampleClass`  to both names.

Because of this internal renaming, you can’t access the attribute or method from outside the class using their original names:

```python
`>>> sample_instance.__attribute
Traceback (most recent call last):
  ...
AttributeError: 'SampleClass' object has no attribute '__attribute'

>>> sample_instance.__method()
Traceback (most recent call last):
  ...
AttributeError: 'SampleClass' object has no attribute '__method'
```
If you try to access  `.__attribute`  and  `.__method()`  using their original names, then you get an  `AttributeError`. That’s because of name mangling, which internally changes the name of these attributes.

Even though Python mangles names that start with two underscores, it doesn’t completely restrict access to those names. You can always access the mangled name:

```python
`>>> sample_instance._SampleClass__attribute
'Hello!'

>>> sample_instance._SampleClass__method()
Hello!
```
You can still access named-mangled attributes or methods using their mangled names, although this is bad practice, and you should avoid it in your code. If you see a name that uses this convention in someone’s code, then don’t try to force the code to use the name from outside its containing class.



### Using Name Mangling in Inheritance

Even though you’ll find many resources out there that claim that name mangling is for creating private attributes, this naming transformation pursues a different goal:  _preventing name clashes in inheritance_. To define non-public members, you should use a single leading underscore, as you’ve done in previous sections.

Name mangling is particularly useful when you want to ensure that a given attribute or method won’t be accidentally overridden in a subclass:

```python
`class A:
    def __init__(self):
        self.__attr = 0

    def __method(self):
        print("A.__attr", self.__attr)

class B(A):
    def __init__(self):
        super().__init__()
        self.__attr = 1  # Doesn't override A.__attr

    def __method(self):  # Doesn't override A.__method()
        print("B.__attr", self.__attr)
```
By using two leading underscores in attribute and method names, you can prevent subclasses from overriding them. If your class is intended to be subclassed, and it has attributes that you don’t want subclasses to use, then consider naming them with double leading underscores. Avoid using name mangling to create private or non-public attributes.

### Dunder Names in Python

In Python, names with double leading and trailing underscores (`__`) have special meaning to the language itself. These names are known as  **dunder**  names, and dunder is short for  **d**ouble  **under**score. In most cases, Python uses dunder names for methods that support a given functionality in the language’s  [data model](https://docs.python.org/3/reference/datamodel.html).

Dunder methods are also known as  [special methods](https://docs.python.org/3/glossary.html#term-special-method), and in some informal circles, they’re called  _magic_  methods. Why  _magic_? Because Python calls them automatically in response to specific actions. For example, when you call the built-in  [`len()`](len-python-function.md)  function with a  `list`  object as an argument, Python calls  `list.__len__()`  under the hood to retrieve the list’s length.

In general, dunder names are reserved for supporting internal Python behaviors. So, you should avoid inventing such names. Instead, you should only use documented dunder names. In the end, creating a custom dunder name won’t have a practical effect because Python only calls those special methods that the language defines.

A few examples of commonly used dunder methods include:


|Special Method  |Description  |
|--|--|
|[`.__init__()`](python-class-constructor.md)  |Provides an initializer in Python classes  |
|[`.__call__()`](python-callable-instances.md)  |Makes the instances of a class callable  |
|[`.__str__()`  and  `.__repr__()`](repr-vs-str.md)  |Provide string representations for objects  |
|[`.__iter__()`  and  `.__next__()`](iterators-iterables.md)  |Support the iterator protocol  |
|[`.__len__()`](len-python-function.md)  |Supports the `len()` function  |

These are just a sample of all the special methods that Python defines. As you can conclude from their descriptions, all these methods support specific Python features. You can provide implementations for these methods in your custom classes so that they support the related features.

To illustrate, say that you want to create a  `ShoppingCart`  class to manage the cart in an online shop. You need this class to support the  `len()`  function, which should return the number of items in the cart. Here’s how you can provide this support:

cart.py

```python
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        return self.products

 def __len__(self):        return len(self.products)
```
 

Your class keeps track of the added products using a  `list`  object. Then, you implement methods for adding a new product to the cart and retrieving the list of current products. The  `.__len__()`  special method returns the number of items in  `.products`  using the built-in  `len()`  function.

By implementing  `.__len__()`, you ensure that your  `ShoppingCart`  class also support the  `len()`  function:

```python
>>> from cart import ShoppingCart

>>> cart = ShoppingCart()
>>> cart.add_product("keyboard")
>>> cart.add_product("mouse")
>>> cart.add_product("monitor")

>>> len(cart)
3
```
In this snippet, you create a shopping cart and add three items. When you call  `len()`  with the  `cart`  instance as an argument, you get the number of items that are currently in the cart.

Finally, Python also has some dunder names that don’t refer to special methods but to special attributes and variables. A couple of the most commonly used ones are the following:

-   [`__name__`](https://docs.python.org/3/reference/import.html#name__)  uniquely identifies the module in the import system.
-   [`__file__`](https://docs.python.org/3/reference/import.html#file__)  indicates the path to the file from which a module was loaded.

You’ll often find  `__name__`  in a common Python idiom that’s closely related to executable  [scripts](run-python-scripts.md). So, in many executable Python files, you’ll see a code snippet that looks like the following:

Python`script.py`

`# ...

def main():
    # Implemention...

if __name__ == "__main__":
    main()
```
The  [name-main idiom](if-name-main-python.md)  allows you to execute code when you run the containing file as a script but not when you import it as a module.


## Other Usages of Underscores in Python

Up to this point, you’ve learned about some Python naming conventions involving either leading or trailing underscores. You’ve learned about public vs non-public names, name mangling, and dunder names.

In this section, you’ll quickly explore other use cases of underscores in Python names. Some of these use cases include the following:

-   Placeholder variable in REPL sessions
-   Throwaway variables in loops and other constructs
-   Wildcards in structural pattern matching
-   Named tuple methods

In the context of a REPL session, the underscore character has an implicit role. It works as a  [special variable](python-repl.md/#using-the-_-special-variable)  containing the result of the last evaluated  [expression](python-operators-expressions.md):

```python
`>>> 12 + 30
42
>>> _
42

>>> pow(4, 2)
16
>>> _
16
```
In these examples, you evaluate two different expressions. Expressions always evaluate to a concrete value, which Python automatically assigns to the  `_`  variable after the evaluation. You can access and use the  `_`  variable as you’d use any other variable:

```python
`>>> numbers = [1, 2, 3, 4]

>>> len(numbers)
4

>>> sum(numbers) / _
2.5
```
In this example, you first create a list of numbers. Then, you call  `len()`  to get the number of values in the list. Python automatically stores this value in the  `_`  variable. Finally, you use  `_`  to compute the average of your list of values.

Throwaway variables are another common use case of underscores in Python names. You’ll often see them in  `for`  loops and comprehensions where you don’t need to use the loop variable in any computation.

To illustrate, say that you want to build a list of lists to represent a five-by-five matrix. Every row will contain integer numbers from  `0`  to  `4`. In this situation, you can use the following  [list comprehension](list-comprehension-python.md):

```python
`>>> matrix = [[number for number in range(5)] for _ in range(5)]

>>> matrix
[
 [0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4]
]
```
In this example, the outer list comprehension,  `[... for _ in range(5)]`, creates five lists. Each list represents a row in the resulting matrix. Note how you’ve used an underscore (`_`) as the loop variable. You do this because you don’t need this variable in the inner list comprehension,  `[number for number in range(5)]`, which fills each row with values.

[Structural pattern matching](python310-new-features.md#structural-pattern-matching)  was introduced to Python in  [version 3.10](python310-new-features.md). It uses a  `match`  …  `case`  construct to compare an object to several different cases. Such statements are effective at deconstructing data structures and picking out individual elements. Python treats a single underscore as a  [wildcard](https://peps.python.org/pep-0636/#adding-a-wildcard)  in a  `case`  statement, so it’ll match anything. You often use it to alert the user that an object doesn’t have the expected structure.

The  [following example](python310-new-features.md/#using-different-kinds-of-patterns)  shows a recursive function that uses pattern matching to sum a list of numbers:

```python
`>>> def sum_list(numbers):
...     match numbers:
...         case []:
...             return 0
...         case [int(first) | float(first), *rest]:
...             return first + sum_list(rest)
...         case  _: ...             raise ValueError(f"can only sum lists of numbers")
...
```
The last  `case`  statement uses the  `_`  wildcard and will match if  `numbers`  isn’t a list with integer and floating point numbers. You can try it in action:

```python
`>>> sum_list([1, 2, 3])
6

>>> sum_list(["x", "y"])
Traceback (most recent call last):
  ...
ValueError: can only sum lists of numbers
```
When you try to sum a list of strings, then your final  `case`  triggers and  [raises](raise-exception.md)  the  `ValueError`.

Finally, have you used  [named tuples](namedtuple.md)  before? They can help you improve the readability of your code by providing named fields to access their items using dot notation. One odd characteristic of named tuples is that some of the attributes and methods in their pubic interface have a leading underscore in their names:

```python
`>>> from collections import namedtuple

>>> Point = namedtuple("Point", "x y")

>>> point = Point(2, 4)
>>> point
Point(x=2, y=4)

>>> dir(point)
[
 ...
 '_asdict', '_field_defaults', '_fields', '_make', '_replace', 'count',
 'index',
 'x',
 'y'
]
```
Besides the  `.count()`  and  `.index()`  methods, which named tuples inherit from  [`tuple`](tuple.md), named tuples provide three additional methods:  `._asdict()`,  `._make()`, and  `._replace()`. They also have two extra attributes,  `._field_defaults`  and  `._fields`.

As you can see in the highlighted lines, all these additional attributes and methods have a leading underscore in their names. Why? The leading underscore prevents name conflicts with custom fields. In this case, there’s a strong reason for breaking the established convention, which suits the Python  [principle](zen-of-python.md)  that  _practicality beats purity_.

To illustrate, say that you have the following named tuple:

```python
`>>> from collections import namedtuple

>>> Car = namedtuple("Car", ["make", "model", "color", "year"])

>>> mustang = Car(make="Ford", model="Mustang", color="Red", year=2022)
>>> mustang.make
'Ford'
```
In this example, if you use the string  `"make"`  as a field name and the named tuple had a  `.make()`  method instead of the  `._make()`  variation, then you’d have overridden the method with your custom field.

**Note:**  Some of the public attributes of named tuples, like  `._field_defaults`  and  `._fields`, may seem less likely to cause name clashes. However, they use the same naming convention for consistency. However, there’s no way to know what the user will do with your code.

Note that the  `namedtuple()`  function will raise an exception if you try to name any of your fields with a leading underscore:

```python
`>>> Car = namedtuple("Car", ["make", "_model", "color", "year"])
Traceback (most recent call last):
  ...
ValueError: Field names cannot start with an underscore: '_model'
```
This behavior of named tuples ensures that you don’t override any of the methods available as part of a named tuple’s API.

# References
[Single and Double Underscores in Python Names](https://realpython.com/python-double-underscore/)