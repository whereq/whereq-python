# Regular Expressions in Python

Regular Expressions, also known as regexes, in Python. A regex is a special sequence of characters that defines a pattern for complex string-matching functionality.

## The re Module
All the regex functions in Python are in the re module. The re module contains many useful functions and methods.


### re.search(<regex>, <string>)

`re.search(<regex>, <string>)`  scans  `<string>`  looking for the **first** location where the pattern  `<regex>`  matches. If a match is found, then  `re.search()`  returns a  **match object**. Otherwise, it returns  [`None`](https://realpython.com/null-in-python/).

`re.search()`  takes an optional third  `<flags>`  argument that you’ll learn about at the end of this tutorial.

### Import re.search()

```python
import re
re.search(...)
```

** Or **
```python
from re import search
search(...)
```

### Pattern Matching
A match object is [**truthy**](python-data-types.md/#boolean-type-boolean-context-and-truthiness), so you can use it in a [Boolean context](python-boolean.md) like a conditional statement:
```python
>>> if re.search('123', s):
...     print('Found a match.')
... else:
...     print('No match.')
...
Found a match.
```

### Python Regex Metacharacters
The real power of regex matching in Python emerges when `<regex>` contains special characters called **metacharacters**.


### Metacharacters Supported by the re Module
| Character(s) | Meaning                                                 |
|--------------|---------------------------------------------------------|
| .            | Matches any single character except newline             |
| ^            | Anchors a match at the start of a string                |
|              | Complements a character class                           |
| $            | Anchors a match at the end of a string                  |
| \*           | Matches zero or more repetitions                        |
| +            | Matches one or more repetitions                         |
| ?            | Matches zero or one repetition                          |
|              | Specifies the non-greedy versions of \*, +, and ?       |
|              | Introduces a lookahead or lookbehind assertion          |
|              | Creates a named group                                   |
| {}           | Matches an explicitly specified number of repetitions   |
| \            | Escapes a metacharacter of its special meaning          |
|              | Introduces a special character class                    |
|              | Introduces a grouping backreference                     |
| \[\]         | Specifies a character class                             |
| \|           | Designates alternation                                  |
| ()           | Creates a group                                         |
| :            |                                                         |
| #            |                                                         |
| =            |                                                         |
| !            | Designate a specialized group                           |
| <>           | Creates a named group                                   |


### Metacharacters That Match a Single Character

The metacharacter sequences in this section try to match a single character from the search string. When the regex parser encounters one of these metacharacter sequences, a match happens if the character at the current parsing position fits the description that the sequence describes.

`[]`

> Specifies a specific set of characters to match.

Characters contained in square brackets (`[]`) represent a  **character class**—an enumerated set of characters to match from. A character class metacharacter sequence will match any single character contained in the class.

You can enumerate the characters individually like this:

```python
>>> re.search('ba[artz]', 'foobarqux')
<_sre.SRE_Match object; span=(3, 6), match='bar'>
>>> re.search('ba[artz]', 'foobazqux')
<_sre.SRE_Match object; span=(3, 6), match='baz'>
```
The metacharacter sequence  `[artz]`  matches any single  `'a'`,  `'r'`,  `'t'`, or  `'z'`  character. In the example, the regex  `ba[artz]`  matches both  `'bar'`  and  `'baz'`  (and would also match  `'baa'`  and  `'bat'`).

A character class can also contain a range of characters separated by a hyphen (`-`), in which case it matches any single character within the range. For example,  `[a-z]`  matches any lowercase alphabetic character between  `'a'`  and  `'z'`, inclusive:

```python
>>> re.search('[a-z]', 'FOObar')
<_sre.SRE_Match object; span=(3, 4), match='b'>
```
`[0-9]`  matches any digit character:

```python
>>> re.search('[0-9][0-9]', 'foo123bar')
<_sre.SRE_Match object; span=(3, 5), match='12'>
```
In this case,  `[0-9][0-9]`  matches a sequence of two digits. The first portion of the string  `'foo123bar'`  that matches is  `'12'`.

`[0-9a-fA-F]`  matches any  [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal)  digit character:

```python
>>> re.search('[0-9a-fA-f]', '--- a0 ---')
<_sre.SRE_Match object; span=(4, 5), match='a'>
```
Here,  `[0-9a-fA-F]`  matches the first hexadecimal digit character in the search string,  `'a'`.

**Note:**  In the above examples, the return value is always the leftmost possible match.  `re.search()`  scans the search string from left to right, and as soon as it locates a match for  `<regex>`, it stops scanning and returns the match.

You can complement a character class by specifying  `^`  as the first character, in which case it matches any character that  _isn’t_  in the set. In the following example,  `[^0-9]`  matches any character that isn’t a digit:

```python
>>> re.search('[^0-9]', '12345foo')
<_sre.SRE_Match object; span=(5, 6), match='f'>
```
Here, the match object indicates that the first character in the string that isn’t a digit is  `'f'`.

If a  `^`  character appears in a character class but isn’t the first character, then it has no special meaning and matches a literal  `'^'`  character:

```python
>>> re.search('[#:^]', 'foo^bar:baz#qux')
<_sre.SRE_Match object; span=(3, 4), match='^'>
```
As you’ve seen, you can specify a range of characters in a character class by separating characters with a hyphen. What if you want the character class to include a literal hyphen character? You can place it as the first or last character or escape it with a backslash (`\`):

```python
>>> re.search('[-abc]', '123-456')
<_sre.SRE_Match object; span=(3, 4), match='-'>
>>> re.search('[abc-]', '123-456')
<_sre.SRE_Match object; span=(3, 4), match='-'>
>>> re.search('[ab\-c]', '123-456')
<_sre.SRE_Match object; span=(3, 4), match='-'>
```
If you want to include a literal  `']'`  in a character class, then you can place it as the first character or escape it with backslash:

```python
>>> re.search('[]]', 'foo[1]')
<_sre.SRE_Match object; span=(5, 6), match=']'>
>>> re.search('[ab\]cd]', 'foo[1]')
<_sre.SRE_Match object; span=(5, 6), match=']'>
```
Other regex metacharacters lose their special meaning inside a character class:

```python
>>> re.search('[)*+|]', '123*456')
<_sre.SRE_Match object; span=(3, 4), match='*'>
>>> re.search('[)*+|]', '123+456')
<_sre.SRE_Match object; span=(3, 4), match='+'>
```
As you saw in the table above,  `*`  and  `+`  have special meanings in a regex in Python. They designate repetition, which you’ll learn more about shortly. But in this example, they’re inside a character class, so they match themselves literally.



dot (`.`)

> Specifies a wildcard.

The  `.`  metacharacter matches any single character except a newline:

```python
>>> re.search('foo.bar', 'fooxbar')
<_sre.SRE_Match object; span=(0, 7), match='fooxbar'>

>>> print(re.search('foo.bar', 'foobar'))
None
>>> print(re.search('foo.bar', 'foo\nbar'))
None
```
As a regex,  `foo.bar`  essentially means the characters  `'foo'`, then any character except newline, then the characters  `'bar'`. The first string shown above,  `'fooxbar'`, fits the bill because the  `.`  metacharacter matches the  `'x'`.

The second and third strings fail to match. In the last case, although there’s a character between  `'foo'`  and  `'bar'`, it’s a newline, and by default, the  `.`  metacharacter doesn’t match a newline. There is, however, a way to force  `.`  to match a newline, which you’ll learn about at the end of this tutorial.

`\w`  
`\W`

> Match based on whether a character is a word character.

`\w`  matches any alphanumeric word character. Word characters are uppercase and lowercase letters, digits, and the underscore (`_`) character, so  `\w`  is essentially shorthand for  `[a-zA-Z0-9_]`:

```python
>>> re.search('\w', '#(.a$@&')
<_sre.SRE_Match object; span=(3, 4), match='a'>
>>> re.search('[a-zA-Z0-9_]', '#(.a$@&')
<_sre.SRE_Match object; span=(3, 4), match='a'>
```
In this case, the first word character in the string  `'#(.a$@&'`  is  `'a'`.

`\W`  is the opposite. It matches any non-word character and is equivalent to  `[^a-zA-Z0-9_]`:

```python
>>> re.search('\W', 'a_1*3Qb')
<_sre.SRE_Match object; span=(3, 4), match='*'>
>>> re.search('[^a-zA-Z0-9_]', 'a_1*3Qb')
<_sre.SRE_Match object; span=(3, 4), match='*'>
```
Here, the first non-word character in  `'a_1*3!b'`  is  `'*'`.

`\d`  
`\D`

> Match based on whether a character is a decimal digit.

`\d`  matches any decimal digit character.  `\D`  is the opposite. It matches any character that  _isn’t_  a decimal digit:

```python
>>> re.search('\d', 'abc4def')
<_sre.SRE_Match object; span=(3, 4), match='4'>

>>> re.search('\D', '234Q678')
<_sre.SRE_Match object; span=(3, 4), match='Q'>
```
`\d`  is essentially equivalent to  `[0-9]`, and  `\D`  is equivalent to  `[^0-9]`.

`\s`  
`\S`

> Match based on whether a character represents whitespace.

`\s`  matches any whitespace character:

```python
>>> re.search('\s', 'foo\nbar baz')
<_sre.SRE_Match object; span=(3, 4), match='\n'>
```
Note that, unlike the dot wildcard metacharacter,  `\s`  does match a newline character.

`\S`  is the opposite of  `\s`. It matches any character that  _isn’t_  whitespace:

```python
>>> re.search('\S', ' \n foo \n ')
<_sre.SRE_Match object; span=(4, 5), match='f'>
```
Again,  `\s`  and  `\S`  consider a newline to be whitespace. In the example above, the first non-whitespace character is  `'f'`.

The character class sequences  `\w`,  `\W`,  `\d`,  `\D`,  `\s`, and  `\S`  can appear inside a square bracket character class as well:

```python
>>> re.search('[\d\w\s]', '---3---')
<_sre.SRE_Match object; span=(3, 4), match='3'>
>>> re.search('[\d\w\s]', '---a---')
<_sre.SRE_Match object; span=(3, 4), match='a'>
>>> re.search('[\d\w\s]', '--- ---')
<_sre.SRE_Match object; span=(3, 4), match=' '>
```
In this case,  `[\d\w\s]`  matches any digit, word, or whitespace character. And since  `\w`  includes  `\d`, the same character class could also be expressed slightly shorter as  `[\w\s]`.
	
# Reference
[Regular Expressions: Regexes in Python (Part 1)](https://realpython.com/regex-python/)
[Regular Expressions: Regexes in Python (Part 2)](https://realpython.com/regex-python-part-2/)