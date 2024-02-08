# F-String for String Interpolation and Formatting

## Doing String Interpolation With F-Strings in Python

F-strings joined the party in Python 3.6 with [PEP 498](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498). Also called **formatted string literals**, f-strings are string literals that have an `f` before the opening quotation mark. They can include Python expressions enclosed in curly braces. Python will replace those expressions with their resulting values. So, this behavior turns f-strings into a string interpolation tool.

### Interpolating Values and Objects in F-Strings

The `f-string` syntax requires starting the string literal with a lowercase or uppercase `f` and then embedding the values, objects, or expressions in curly brackets at specific places:
```python
>>> name = "Foo Bar"
>>> age = 37

>>> f"Hello, {name}! You're {age} years old."
'Hello, Foo Bar! You're 37 years old.'
```

It’s important to note that Python evaluates f-strings at runtime. So, in this example, both `name` and `age` are interpolated into the string literal when Python runs the line of code containing the f-string. Python can only interpolate these variables because you defined them _before_ the f-string, which means that they must be in [scope](https://realpython.com/python-namespaces-scope/) when Python evaluates the f-string.

### Embedding Expressions in F-Strings
The `f-strings` are incredibly powerful. They allow for the inclusion of Python expressions, such as [function](https://realpython.com/defining-your-own-python-function/) and method calls, as well as [comprehensions](https://realpython.com/list-comprehension-python/) or other more complex expressions:
```python
>>> name = "Foo Bar"
>>> age = 37

>>> f"Hello, {name.upper()}! You're {age} years old."
"Hello, FOO BAR! You're 37 years old."

>>> f"{[2**n for n in range(3, 9)]}"
'[8, 16, 32, 64, 128, 256]'
```

In the first f-string, you embed a call to the `.upper()` string method in the first replacement field. Python runs the method call and inserts the uppercased name into the resulting string. In the second example, you create an f-string that embeds a [list comprehension](https://realpython.com/list-comprehension-python/). The comprehension creates a new list of powers of `2`.

### Formatting Strings With Python’s F-String
The expressions that you embed in an f-string are evaluated at runtime. Then, Python formats the result using the [`.__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__) special method under the hood. This method supports the string formatting [protocol](python-classes.md/#special-methods-and-protocols). This protocol underpins both the `.format()` method, which you already saw, and the built-in [`format()`](https://docs.python.org/3/library/functions.html#format) function:

The `f-string` formats the provided value based on the **format specifier**, adhering to the guidelines of the string formatting mini-language.

```python
>>> balance = 5425.9292

>>> f"Balance: ${balance:.2f}"
'Balance: $5425.93'

>>> heading = "Centered string"
>>> f"{heading:=^30}"
'=======Centered string========'
```

**More examples**

```python
>>> integer = -1234567
>>> f"Comma as thousand separators: {integer:,}"
'Comma as thousand separators: -1,234,567'

>>> sep = "_"
>>> f"User's thousand separators: {integer:{sep}}"
'User's thousand separators: -1_234_567'

>>> floating_point = 1234567.9876
>>> f"Comma as thousand separators and two decimals: {floating_point:,.2f}"
'Comma as thousand separators and two decimals: 1,234,567.99'

>>> date = (9, 6, 2023)
>>> f"Date: {date[0]:02}-{date[1]:02}-{date[2]}"
'Date: 09-06-2023'

>>> from datetime import datetime
>>> date = datetime(2023, 9, 26)
>>> f"Date: {date:%m/%d/%Y}"
'Date: 09/26/2023'
```
**Note** how in the second example, curly brackets were utilized to incorporate variables or expressions within the **format specifiers**. This flexibility allows for the creation of dynamic specifiers, which is quite advantageous. In the last example, a [`datetime`](python-datetime.md) object was formatted, which can be customized using special [date format specifiers](https://strftime.org/).

# References
[Python's F-String for String Interpolation and Formatting](https://realpython.com/python-f-strings/)