# Regular Expressions in Python

Regular Expressions, also known as regexes, in Python. A regex is a special sequence of characters that defines a pattern for complex string-matching functionality.

## The re Module
All the regex functions in Python are in the re module. The re module contains many useful functions and methods.


### re.search(<regex>, <string>)

`re.search(<regex>, <string>)`  scans  `<string>`  looking for the **first** location where the pattern  `<regex>`  matches. If a match is found, then  `re.search()`  returns a  **match object**. Otherwise, it returns  [`None`](https://realpython.com/null-in-python/).

`re.search()`  takes an optional third  `<flags>`  argument that you’ll learn about at the end of this tutorial.