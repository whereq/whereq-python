# Operators and Expressions in Python

## Operators

-   **Assignment**  operators
-   **Arithmetic**  operators
-   **Comparison**  operators
-   **Boolean**  or logical operators
-   **Identity**  operators
-   **Membership**  operators
-   **Concatenation**  and  **repetition**  operators
-   **Bitwise**  operators


## Arithmetic Operators and Expressions


|Operator  |Type  |Operation  |Sample Expression  |Result  |
|--|--|--|--|--|
|/  |Binary  |Division  |a / b  |The quotient of a divided by b, expressed as a float  |
|//  |Binary  |Floor division or integer division  |a // b  |The quotient of `a` divided by `b`, rounded to the next smallest whole number  |
|**  |Binary  |Exponentiation  |a**b  |`a` raised to the power of `b`  |

```python
>>> 10 / 5
2.0

>>> 10.0 / 5
2.0
```
In the first example, `10` is evenly divisible by `5`. Therefore, this operation could return the integer `2`. However, it returns the floating-point number `2.0`. In the second example, `10.0` is a floating-point number, and `5` is an integer. In this case, Python internally promotes `5` to `5.0` and runs the division. The result is a floating-point number too.

**Note:**  With complex numbers, the division operator doesn’t return a floating-point number but a complex one:

```python
>>> 10 / 5j
-2j
``` 

Here, you run a division between an integer and a complex number. In this case, the standard division operator returns a complex number.


Finally, consider the following examples of using the floor division (`//`) operator:


```python
>>> 10 // 4
2
>>> -10 // -4
2

>>> 10 // -4
-3
>>> -10 // 4
-3
``` 

Floor division always  [rounds down](https://realpython.com/python-rounding/#rounding-down). This means that the result is the greatest integer that’s smaller than or equal to the quotient. For positive numbers, it’s as though the fractional portion is truncated, leaving only the integer portion.

## Comparison Operators and Expressions in Python
### Comparison of Floating-Point Values

Comparing floating-point numbers is a bit  [more complicated](https://realpython.com/python-numbers/#make-python-lie-to-you)  than comparing integers. The value stored in a  `float`  object may not be precisely what you’d think it would be. For that reason, it’s bad practice to compare floating-point values for exact equality using the  `==`  operator.

Consider the example below:


```python
>>> x = 1.1 + 2.2
>>> x == 3.3
False

>>> 1.1 + 2.2
3.3000000000000003
``` 

Yikes! The internal representation of this addition isn’t exactly equal to  `3.3`, as you can see in the final example. So, comparing  `x`  to  `3.3`  with the equality operator returns  `False`.

To compare floating-point numbers for equality, you need to use a different approach. The preferred way to determine whether two floating-point values are equal is to determine whether they’re close to one another, given some tolerance.

The  `math`  module from the standard library provides a function conveniently called  `isclose()`  that will help you with  `float`  comparison. The function takes two numbers and tests them for approximate equality:


```python
>>> from math import isclose

>>> x = 1.1 + 2.2

>>> isclose(x, 3.3)
True
``` 

In this example, you use the  `isclose()`  function to compare  `x`  and  `3.3`  for approximate equality. This time, you get  `True`  as a result because both numbers are close enough to be considered equal.

## Boolean Operators and Expressions in Python
### Boolean Expressions Involving Boolean Operands

Python built-in and custom functions that return a Boolean value. This type of function is known as a [predicate](https://realpython.com/python-return-statement/#returning-true-or-false) function. The built-in [`all()`](https://realpython.com/python-all/), [`any()`](https://realpython.com/any-python/), [`callable()`](https://docs.python.org/3/library/functions.html#callable), and [`isinstance()`](https://docs.python.org/3/library/functions.html?highlight=built#isinstance) functions are all good examples of this practice.

```python
>>> number = 42

>>> validation_conditions = (
...     isinstance(number, int),
...     number % 2 == 0,
... )

>>> all(validation_conditions)
True

>>> callable(number)
False
>>> callable(print)
True
```

In this code snippet, you first define a variable called  `number`  using your old friend the assignment operator. Then you create another variable called  `validation_conditions`. This variable holds a tuple of expressions. The first expression uses  `isinstance()`  to check whether  `number`  is an integer value.

The second is a compound expression that combines the modulo (`%`) and equality (`==`) operators to create a condition that checks whether the input value is an even number. In this condition, the modulo operator returns the remainder of dividing  `number`  by  `2`, and the equality operator compares the result with  `0`, returning  `True`  or  `False`  as the comparison’s result.

Then you use the  `all()`  function to determine if all the conditions are true. In this example, because  `number = 42`, the conditions are true, and  `all()`  returns  `True`. You can play with the value of  `number`  if you’d like to experiment a bit.

In the final two examples, you use the  `callable()`  function. As its name suggests, this function allows you to determine whether an object is  **callable**. Being callable means that you can call the object with a pair of parentheses and appropriate arguments, as you’d call any Python function.

The  `number`  variable isn’t callable, and the function returns  `False`, accordingly. In contrast, the  `print()`  function is callable, so  `callable()`  returns  `True`.

All the previous discussion is the basis for understanding how the Python logical operators work with Boolean operands.

### Boolean Expressions Involving Other Types of Operands


**Note:** Boolean expressions that [combine two Boolean operands](https://realpython.com/python-operators-expressions/#boolean-expressions-involving-boolean-operands) are a special case of a more general rule that allows you to use the logical operators with all kinds of operands. In every case, you’ll get one of the operands as a result.



|If `x` is|`x and y` returns  |
|--|--|
|Truthy  |y  |
|Falsy|either x or y which one caused the Falsy  |


```python
>>> 3 and 4
4

>>> 0 and 4
0

# The left-hand operand (3) is truthy. Therefore Python needs to evaluate the right-hand operand to make a conclusion. As a result, the right-hand operand, no matter what its truth value is.
>>> 3 and 0 
0

>>> 'a' and 'b'
'b'
>>> '' and 'b'
''
>>> 'a' and ''
''

```


```python
# In this specific expression, both operands are falsy. So, the or operator returns the right-hand operand, and the whole expression is falsy as a result.
>>> 0 or []
[]
```


## Idioms That Exploit Short-Circuit Evaluation
As you dig into Python, you’ll find that there are some common idiomatic patterns that exploit short-circuit evaluation for conciseness of expression, performance, and safety. For example, you can take advantage of this type of evaluation for:

-   Avoiding an exception
-   Providing a default value
-   Skipping a costly operation

To illustrate the first point, suppose you have two variables,  `a`  and  `b`, and you want to know whether the division of  `b`  by  `a`  results in a number greater than  `0`. In this case, you can run the following expression or condition:

```python
>>> a = 3
>>> b = 1

>>> (b / a) > 0
True
```

This code works. However, you need to account for the possibility that  `a`  might be  `0`, in which case you’ll get an  [exception](https://realpython.com/python-exceptions/):

```python
>>> a = 0
>>> b = 1

>>> (b / a) > 0
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```
In this example, the divisor is  `0`, which makes Python raise a  `ZeroDivisionError`  exception. This exception breaks your code. You can skip this error with an expression like the following:

```python
>>> a = 0
>>> b = 1

>>> a != 0 and (b / a) > 0
False
```
When  `a`  is  `0`,  `a != 0`  is false. Python’s short-circuit evaluation ensures that the evaluation stops at that point, which means that  `(b / a)`  never runs, and the error never occurs.

Using this technique, you can implement a function to determine whether an integer is divisible by another integer:

```python
def is_divisible(a, b):
    return b != 0 and a % b == 0
```
In this function, if  `b`  is  `0`, then  `a / b`  isn’t defined. So, the numbers aren’t divisible. If  `b`  is different from  `0`, then the result will depend on the remainder of the division.

Selecting a default value when a specified value is falsy is another idiom that takes advantage of the short-circuit evaluation feature of Python’s logical operators.

For example, say that you have a variable that’s supposed to contain a country’s name. At some point, this variable can end up holding an empty string. If that’s the case, then you’d like the variable to hold a default county name. You can also do this with the  `or`  operator:

```python
>>> country = "Canada"
>>> default_country = "United States"

>>> country or default_country
'Canada'

>>> country = ""
>>> country or default_country 'United States'
```
If  `country`  is non-empty, then it’s truthy. In this scenario, the expression will return the first truthy value, which is  `country`  in the first  `or`  expression. The evaluation stops, and you get  `"Canada"`  as a result.

On the other hand, if  `country`  is an empty  [string](https://realpython.com/python-strings/), then it’s falsy. The evaluation continues to the next operand,  `default_country`, which is truthy. Finally, you get the default country as a result.

Another interesting use case for short-circuit evaluation is to avoid costly operations while creating compound logical expressions. For example, if you have a costly operation that should only run if a given condition is false, then you can use  `or`  like in the following snippet:

```python
data_is_clean or clean_data(data)
```
In this construct, your  `clean_data()`  function represents a costly operation. Because of short-circuit evaluation, this function will only run when  `data_is_clean`  is false, which means that your data isn’t clean.

Another variation of this technique is when you want to run a costly operation if a given condition is true. In this case, you can use the  `and`  operator:

```python
data_is_updated and process_data(data)
```
In this example, the  `and`  operator evaluates  `data_is_updated`. If this variable is true, then the evaluation continues, and the  `process_data()`  function runs. Otherwise, the evaluation stops, and  `process_data()`  never runs.



## Conditional Expressions or the Ternary Operator
Python has what it calls  [conditional expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions). These kinds of expressions are inspired by the  [ternary operator](https://en.wikipedia.org/wiki/Ternary_conditional_operator)  that looks like  `a ? b : c`  and is used in other programming languages. This construct evaluates to  `b`  if the value of  `a`  is true, and otherwise evaluates to  `c`. Because of this, sometimes the equivalent Python syntax is also known as the ternary operator.

However, in Python, the expression looks more readable:

```python
variable = expression_1 if condition else expression_2
```
This expression returns  `expression_1`  if the condition is true and  `expression_2`  otherwise. Note that this expression is equivalent to a regular conditional like the following:

```python
if condition:
    variable = expression_1
else:
    variable = expression_2
```
So, why does Python need this syntax?  [PEP 308](https://peps.python.org/pep-0308/)  introduced conditional expressions as an effort to avoid the prevalence of error-prone attempts to achieve the same effect of a traditional ternary operator using the  `and`  and  `or`  operators in an expression like the following:

```python
variable = condition and expression_1 or expression_2
```
However, this expression doesn’t work as expected, returning  `expression_2`  when  `expression_1`  is falsy.

Some Python developers would avoid the syntax of conditional expressions in favor of a regular conditional statement. In any case, this syntax can be handy in some situations because it provides a concise tool for writing two-way conditionals.

Here’s an example of how to use the conditional expression syntax in your code:

```python
>>> day = "Sunday"
>>> open_time = "11AM" if day == "Sunday" else "9AM"
>>> open_time
'11AM'

>>> day = "Monday"
>>> open_time = "11AM" if day == "Sunday" else "9AM"
>>> open_time
'9AM'
```
When  `day`  is equal to  `"Sunday"`, the condition is true and you get the first expression,  `"11AM"`, as a result. If the condition is false, then you get the second expression,  `"9AM"`. Note that similarly to the  `and`  and  `or`  operators, the conditional expression returns the value of one of its expressions rather than a Boolean value.


## Concatenation and Repetition Operators and Expressions

|Operator  |Operation  |Sample Expression  |Result  |
|--|--|--|--|
|+  |Concatenation |seq_1 + seq_2  |A new sequence containing all the items from both operands  |
|*  |Repetition |seq * n  |A new sequence containing the items of `seq` repeated `n` times  |

```python
>>> "Hello, " + "World!"
'Hello, World!'

>>> ("A", "B", "C") + ("D", "E", "F")
('A', 'B', 'C', 'D', 'E', 'F')

>>> [0, 1, 2, 3] + [4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]
```


## The Walrus Operator and Assignment Expressions
Regular assignment statements with the `=` operator don’t have a return value. The assignment operator creates or updates variables. Because of this, the operator can’t be part of an expression.

Since [Python 3.8](https://realpython.com/python38-new-features/), there is a new type of assignment. This new assignment is called **assignment expression** or **named expression**. The new operator is called the **walrus operator**, and it’s the combination of a colon and an equal sign (`:=`).

Unlike regular assignments, assignment expressions do have a return value, which is why they’re  _expressions_. So, the operator accomplishes two tasks:

1.  Returns the expression’s result
2.  Assigns the result to a variable

The walrus operator is also a binary operator. Its left-hand operand must be a variable name, and its right-hand operand can be any Python expression. The operator will evaluate the expression, assign its value to the target variable, and return the value.

The general syntax of an assignment expression is as follows:

```python
(variable := expression)
```
This expression looks like a regular assignment. However, instead of using the assignment operator (`=`), it uses the walrus operator (`:=`). For the expression to work correctly, the enclosing parentheses are required in most use cases. However, in certain situations, you won’t need them. Either way, they won’t hurt you, so it’s safe to use them.

Assignment expressions come in handy when you want to reuse the result of an expression or part of an expression without using a dedicated assignment to grab this value beforehand. It’s particularly useful in the context of a conditional statement. To illustrate, the example below shows a toy function that checks the length of a string object:

```python
>>> def validate_length(string):
...     if (n := len(string)) < 8: ...         print(f"Length {n} is too short, needs at least 8")
...     else:
...         print(f"Length {n} is okay!")
...

>>> validate_length("Pythonista")
Length 10 is okay!

>>> validate_length("Python")
Length 6 is too short, needs at least 8
```
In this example, you use a conditional statement to check whether the input string has fewer than  `8`  characters.

The assignment expression,  `(n := len(string))`, computes the string length and assigns it to  `n`. Then it returns the value that results from calling  `len()`, which finally gets compared with  `8`. This way, you guarantee that you have a reference to the string length to use in further operations.

### Walrus Operator Use Case
1. `if-else` expression
- normal
```python
a = 15
if a > 10:
    print('hello, walrus operator!')
```

- walrus operator
```python
if (a := 15) > 10:
    print('hello, walrus operator!')
```

2. 'while' loop
- normal
```python
n = 5
while n:
    print('hello, walrus operator!')
    n -= 1
```

- walrus operator
```python
n = 5
while (n := n - 1) + 1: # Adding 1 is necessary because n is decremented by 1 before the output is executed.
    print('hello, walrus operator!')
```

- normal
```python
while True:
    psw = input("Please input pwd：")
    if psw == "123":
        break
```

- walrus operator
```python
while (psw := input("Please input pwd：")) != "123":
    continue
```

- normal
```python
fp = open("test.txt", "r")
while True:
    line = fp.readline()
    if not line:
        break
    print(line.strip())
fp.close()
```

- walrus
```python
fp = open("test.txt", "r")
while line := fp.readline():
    print(line.strip())
```

3. Used for list comprehensions
Calculate the square root of elements, and retain values where the square root is greater than 5:
- normal
```python
nums = [16, 36, 49, 64]
def f(x):
    print('The function f(x) was executed once.')
    return x ** 0.5
print([f(i) for i in nums if f(i) > 5])
```
**Output**
```python
The function f(x) was executed once.
The function f(x) was executed once.
The function f(x) was executed once.
The function f(x) was executed once.
The function f(x) was executed once.
The function f(x) was executed once.
The function f(x) was executed once.
[6.0, 7.0, 8.0]
```
There are only 4 numbers, but the function was executed 7 times. This is because three numbers satisfy the condition of the list comprehension, requiring an additional 3 calculations. **When the program data is huge, this will waste a lot of performance.**

- walrus
```python
nums = [16, 36, 49, 64]
def f(x):
    print('The function f(x) was executed once.')
    return x ** 0.5
print([n for i in nums if (n := f(i)) > 5])
```
**Output**
```python
The function f(x) was executed once.
The function f(x) was executed once.
The function f(x) was executed once.
The function f(x) was executed once.
[6.0, 7.0, 8.0]
```

The function was only executed 4 times, and the function execution results were stored in 'n', so no additional calculations were needed. Performance is better than without using ':='.

Of course, the walrus operator is also suitable for use in `dictionary` comprehensions and `set` comprehensions.

### Walrus Operator Conclusion
**Using the walrus operator in appropriate scenarios can reduce program complexity and simplify code. On one hand, it enables writing elegant and concise Python code; on the other hand, it aids in understanding others' code. In some cases, it can even improve program performance.**

# References
[Operators and Expressions in Python](https://realpython.com/python-operators-expressions/)