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

## Other Relevant Features of F-Strings

###Using an Object’s String Representations in F-Strings
Python’s f-strings support two flags with special meaning in the interpolation process. These flags are closely related to how Python manages the [string representation](../dive-deeper/__repr__vs__str__.md/#how-can-you-access-an-objects-string-representations) of objects. These flags are:

|Flag  |Description  |
|--|--|
|!s  |Interpolates the string representation from the `.__str__()` method  |
|!r  |Interpolates the string representation from the `.__repr__()` method  |

The  `.__str__()`  [special method](python-classes/#special-methods-and-protocols)  generally provides a user-friendly string representation of an object, while the  `.__repr__()`  method returns a developer-friendly representation. To illustrate how these methods work under the hood, consider the following class:

```python
# person.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I'm {self.name}, and I'm {self.age} years old."

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', age={self.age})"
```

This class has two  [instance attributes](python-classes/#instance-attributes),  `.name`  and  `.age`. The  `.__str__()`  method returns a string that consists of an informative message for users of your class. This message should be useful for end users rather than developers.

**Note:**  To dive deeper into the  `__str__()`  and  `__repr__()`  methods, check out  [When Should You Use.  `.__repr__()`  vs  `.__str__()`  in Python?](../dive-deeper/__repr__vs__str__.md)

In contrast, the  `.__repr__()`  method returns a string that’s a developer-friendly representation of the object. In short, the representation tells the developer how the current instance was created. Ideally, the developer should be able to copy this string representation and create an equivalent object.

How does this discussion about string representation affect f-strings? When you create your f-strings, you can choose which string representation to use with the  `!r`  and  `!s`  flags:

```python
>>> from person import Person

>>> fooBar = Person("Foo Bar", 25)

>>> f"{fooBar!s}"
"I'm Foo Bar, and I'm 25 years old."

>>> f"{fooBar!r}"
"Person(name='Foo Bar', age=25)"
```
In the first f-string, you use the  `!s`  tag to interpolate the string representation that  `.__str__()`  returns. In the second f-string, you use the  `!r`  flag to interpolate the developer-friendly string representation of your current object.

These two flags are pretty relevant for you as a Python developer. Depending on your code’s intended audience, you can decide which one to use. In general, it should be the one that provides more value to your users.

It’s important to note that the  `%`  operator also supports equivalent conversion types,  `s`  and  `r`, which work the same as the  `!s`  and  `!r`  flags in f-strings.

### Self-Documenting Expressions for Debugging
F-strings offer an additional noteworthy feature that proves particularly beneficial during the debugging phase. This feature aids in self-documenting expressions, which can be invaluable when troubleshooting. For instance, suppose you encounter a minor bug or issue in your code. In such scenarios, you may need to ascertain the value of a variable at a specific moment during the code's execution.

```python
>>> variable = "Some mysterious value"

>>> print(f"{variable = }")
variable = 'Some mysterious value'
```

In an `f-string`, it will be very easy to employ a variable name followed by an equal sign (=) to craft a self-explanatory expression. When Python processes the `f-string`, it constructs a string resembling an expression, incorporating the variable's name, the equal sign, and the variable's present value. This attribute of `f-strings` proves beneficial for swiftly incorporating debugging checks into the code.

Note that the whitespaces around the equal sign aren’t required but they are reflected in the output:

```python
>>> print(f"{variable=}")
variable='Some mysterious value'

>>> print(f"{variable= }")
variable= 'Some mysterious value'

>>> print(f"{variable =}")
variable ='Some mysterious value'
```

Even though the whitespaces aren’t required, they can improve your code’s readability and the output’s format.


### Comparing Performance: F-String vs Traditional Tools
```python
# performance.py

import timeit

name = "Foo Bar"
age = 40
strings = {
    "Modulo operator": "'Name: %s Age: %s' % (name, age)",
    ".format() method": "'Name: {} Age: {}'.format(name, age)",
    "f_string": "f'Name: {name} Age: {age}'",
}

def run_performance_test(strings):
    max_length = len(max(strings, key=len))
    for tool, string in strings.items():
        time = timeit.timeit(
            string,
            number=1000000,
            globals=globals()
        ) * 1000
        print(f"{tool}: {time:>{max_length - len(tool) + 6}.2f} ms")

run_performance_test(strings)
```
**Output**
```
Modulo operator:  142.56 ms
.format() method: 256.08 ms
f_string:         141.54 ms
```

This output shows that f-strings are a bit faster than the `%` operator and the `.format()` method, which is the slowest tool because of all the required function calls. So, f-strings are readable, concise, and also fast.

### Using Traditional String Formatting Tools Over F-Strings

#### Dictionary Interpolation
Interpolating dictionary values into a string may be a common requirement in your code. Because you now know that `f-strings` are neat, you may think of using them for this task. You end up with a piece of code that looks like the following:

```python
>>> person = {"name": "Jane Doe", "age": 25}

>>> f"Hello, {person['name']}! You're {person['age']} years old."
"Hello, Jane Doe! You're 25 years old."
```
That’s great! The code works just fine. However, it doesn’t look clean because of all those dictionary key lookups embedded in the string. The `f-string` looks cluttered and may be hard to read. How about using the  `.format()`  method?

Here’s a new version of your code:

```python
>>> "Hello, {name}! You're {age} years old.".format(**person)
"Hello, Jane Doe! You're 25 years old."

>>> "Hello, {name}!".format(**person)
'Hello, Jane Doe!'
```
In this example, you use direct names instead of dictionary lookups in the replacement fields. The only additional requirement is that you need to use the `dictionary unpacking operator` (`**`) in the call to  `.format()`. Now, the string looks cleaner and is also a bit shorter than the version using an `f-string`.

As an additional gain, it’s important to note that the number of replacement fields in the string doesn’t have to match the number of keys in the input dictionary. The  `.format()`  method will ignore unnecessary keys.

You also have the option of using the modulo operator, though:

```python
>>> "Hello, %(name)s! You're %(age)s years old." % person
"Hello, Jane Doe! You're 25 years old."

>>> "Hello, %(name)s!" % person
'Hello, Jane Doe!'
```
This time, the string is even shorter. You use direct names in the replacement fields and don’t have to use the `dictionary unpacking operator` because the **modulo operator unpacks the dictionary** for you. However, some may say that the replacement fields aren’t that readable and that the modulo operator has limited formatting capabilities.

So, what version do you prefer? Share your thoughts in the comments!


#### SQL Database Queries

Using any string interpolation tool is a bad idea when you’re building SQL queries with dynamic parameters. In this scenario, interpolation tools invite [SQL injection attacks](https://realpython.com/prevent-python-sql-injection/).

```python
import psycopg2

connection = psycopg2.connect(
    database="db",
    user="user",
    password="password"
)
cursor = connection.cursor()

role = "admin"

query_modulo = "SELECT * FROM users WHERE role = '%s'" % role
query_format = "SELECT * FROM users WHERE role = '{role}'".format(role=role)
query_f_string = f"SELECT * FROM users WHERE role = '{role}'"

cursor.execute(query_modulo)
cursor.execute(query_format)
cursor.execute(query_f_string)
```

All of these strings directly insert the query parameter into the final query without any validation or security check. If you run any of these queries using the `.execute()` method, then the database won’t be able to perform any security checks on the parameters, which makes your code prone to SQL injection attacks.

To avoid the risk of SQL injection, you can use the  `%`  operator syntax to build the query template and then provide the query parameter as the second argument to the  `.execute()`  method in a tuple or list:

```python
query_template = "SELECT * FROM users WHERE role = %s" 
cursor.execute(query_template, (role,))
```
In this example, you use the  `%`  operator syntax to create the query template. Then, you provide the parameters as an independent argument to  `.execute()`. In this case, the database system will use the specified type and value of  `role`  when executing the query. This practice offers protection against SQL injection.

**Note:**  You should only use the modulo operator syntax in the string literal that represents the query template. You shouldn’t use the operator and the actual sequence of parameters to build the final query. Just let  `.execute()`  do the hard work and build the final query for you in a safer way.

In short, you must avoid using any string interpolation tool to build dynamic queries beforehand. Instead, use the  `%`  operator syntax to build the query template and pass the query parameters to  `.execute()`  in a sequence.

#### Internationalization and Localization

When you want to provide  [internationalization and localization](https://en.wikipedia.org/wiki/Internationalization_and_localization)  in a Python project, the  `.format()`  method is the way to go:

```python
>>> greeting_template = "{greeting} Pythonista!"

>>> greeting_en = "Good Morning!"
>>> greeting_es = "¡Buenos días!"
>>> greeting_fr = "Bonjour!"

>>> for greeting in (greeting_en, greeting_es, greeting_fr):
...     print(greeting_template.format(greeting=greeting))
...
Good Morning! Pythonista!
¡Buenos días! Pythonista!
Bonjour! Pythonista!
```
You can support multiple languages using string templates. Then, you can handle localized string formatting based on the user’s locale. The  `.format()`  method will allow you to dynamically interpolate the appropriate strings depending on the user’s language selection.



# References
[Python's F-String for String Interpolation and Formatting](https://realpython.com/python-f-strings/)
[Format Specification Mini-Language]（https://docs.python.org/3/library/string.html#formatspec）