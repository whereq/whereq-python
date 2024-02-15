# Python Datetime



## Using the Python  `datetime`  Module[]

As you can see, working with dates and times in programming can be complicated. Fortunately, you rarely need to implement complicated features from scratch these days since many open-source libraries are available to help out. This is definitely the case in Python, which includes three separate modules in the standard library to work with dates and times:

1.  **[`calendar`](https://docs.python.org/3/library/calendar.html#module-calendar)**  outputs calendars and provides functions using an idealized  [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar).
2.  **[`datetime`](https://docs.python.org/3/library/datetime.html)**  supplies classes for manipulating dates and times.
3.  **[`time`](https://docs.python.org/3/library/time.html)**  provides time-related functions where dates are not needed.

In this tutorial, you’ll focus on using the Python  **`datetime`**  module. The main focus of  `datetime`  is to make it less complicated to access attributes of the object related to dates, times, and time zones. Since these objects are so useful,  `calendar`  also returns instances of classes from  `datetime`.

[`time`](time-module.md)  is less powerful and more complicated to use than  `datetime`. Many functions in  `time`  return a special  [**`struct_time`**](https://docs.python.org/3/library/time.html#time.struct_time)  instance. This object has a  [named tuple](namedtuple.md)  interface for accessing stored data, making it similar to an instance of  `datetime`. However, it doesn’t support all of the features of  `datetime`, especially the ability to perform arithmetic with time values.

`datetime`  provides three classes that make up the high-level interface that most people will use:

1.  **[`datetime.date`](https://docs.python.org/3/library/datetime.html#date-objects)**  is an idealized date that assumes the Gregorian calendar extends infinitely into the future and past. This object stores the  `year`,  `month`, and  `day`  as attributes.
2.  **[`datetime.time`](https://docs.python.org/3/library/datetime.html#time-objects)**  is an idealized time that assumes there are 86,400 seconds per day with no leap seconds. This object stores the  `hour`,  `minute`,  `second`,  `microsecond`, and  `tzinfo`  (time zone information).
3.  **[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects)**  is a combination of a  `date`  and a  `time`. It has all the attributes of both classes.



### Creating Python  `datetime`  Instances

The three classes that represent dates and times in  `datetime`  have similar  **initializers**. They can be  [instantiated](object-oriented-programming.md/#how-do-you-instantiate-a-class-in-python)  by passing keyword arguments for each of the attributes, such as  `year`,  `date`, or  `hour`. You can try the code below to get a sense of how each object is created:

```python
`>>> from datetime import date, time, datetime
>>> date(year=2020, month=1, day=31)
datetime.date(2020, 1, 31)
>>> time(hour=13, minute=14, second=31)
datetime.time(13, 14, 31)
>>> datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31)
datetime.datetime(2020, 1, 31, 13, 14, 31)
```
In this code, you  [import](absolute-vs-relative-python-imports.md)  the three main classes from  `datetime`  and  **instantiate**  each of them by passing arguments to the constructor. You can see that this code is somewhat verbose, and if you don’t have the information you need as  [integers](integers.md), these techniques can’t be used to create  `datetime`  instances.

Fortunately,  `datetime`  provides several other convenient ways to create  `datetime`  instances. These methods don’t require you to use integers to specify each attribute, but instead allow you to use some other information:

1.  **[`date.today()`](https://docs.python.org/3/library/datetime.html#datetime.date.today)**  creates a  `datetime.date`  instance with the current local date.
2.  **[`datetime.now()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.now)**  creates a  `datetime.datetime`  instance with the current local date and time.
3.  **[`datetime.combine()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.combine)**  combines instances of  `datetime.date`  and  `datetime.time`  into a single  `datetime.datetime`  instance.

These three ways of creating  `datetime`  instances are helpful when you don’t know in advance what information you need to pass into the basic initializers. You can try out this code to see how the alternate initializers work:

```python
`>>> from datetime import date, time, datetime
>>> today = date.today()
>>> today
datetime.date(2020, 1, 24)
>>> now = datetime.now()
>>> now
datetime.datetime(2020, 1, 24, 14, 4, 57, 10015)
>>> current_time = time(now.hour, now.minute, now.second)
>>> datetime.combine(today, current_time)
datetime.datetime(2020, 1, 24, 14, 4, 57)
```
In this code, you use  `date.today()`,  `datetime.now()`, and  `datetime.combine()`  to create instances of  `date`,  `datetime`, and  `time`  objects. Each instance is stored in a different  [variable](variables.md):

1.  **`today`**  is a  `date`  instance that has only the year, month, and day.
2.  **`now`**  is a  `datetime`  instance that has the year, month, day, hour, minute, second, and microseconds.
3.  **`current_time`**  is a  `time`  instance that has the hour, minute, and second set to the same values as  `now`.

On the last line, you combine the date information in  `today`  with the time information in  `current_time`  to produce a new  `datetime`  instance.

**Warning:**  `datetime`  also provides  `datetime.utcnow()`, which returns an instance of  `datetime`  at the current UTC. However, the Python  [documentation](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow)  recommends against using this method because it doesn’t include any time zone information in the resulting instance.

Using  `datetime.utcnow()`  may produce some  [surprising results](https://blog.ganssle.io/articles/2019/11/utcnow.html)  when doing arithmetic or comparisons between  `datetime`  instances. In a  [later section](python-datetime.md/#working-with-time-zones), you’ll see how to assign time zone information to  `datetime`  instances.

### Using Strings to Create Python  `datetime`  Instances[](python-datetime.md/#using-strings-to-create-python-datetime-instances "Permanent link")

Another way to create  `date`  instances is to use  [`.fromisoformat()`](https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat). To use this method, you provide a  [string](python-strings/)  with the date in the ISO 8601 format that you learned about  [earlier](python-datetime/#how-standard-dates-can-be-reported). For instance, you might provide a string with the year, month, and date specified:

Text

`2020-01-31
```
This string represents the date January 31, 2020, according to the ISO 8601 format. You can create a  `date`  instance with the following example:

```python
`>>> from datetime import date
>>> date.fromisoformat("2020-01-31")
datetime.date(2020, 1, 31)
```
In this code, you use  `date.fromisoformat()`  to create a  `date`  instance for January 31, 2020. This method is very useful because it’s based on the ISO 8601 standard. But what if you have a string that represents a date and time but isn’t in the ISO 8601 format?

Fortunately, Python  `datetime`  provides a method called  [`.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime)  to handle this situation. This method uses a special  **mini-language**  to tell Python which parts of the string are associated with the  `datetime`  attributes.

To construct a  `datetime`  from a string using  `.strptime()`, you have to tell Python what each of the parts of the string represents using formatting codes from the mini-language. You can try this example to see how  `.strptime()`  works:

```python
 1>>> date_string = "01-31-2020 14:45:37"
 2>>> format_string = "%m-%d-%Y %H:%M:%S"
```
On  **line 1**, you create  `date_string`, which represents the date and time January 31, 2020, at 2:45:37 PM. On  **line 2**, you create  `format_string`, which uses the mini-language to specify how the parts of  `date_string`  will be turned into  `datetime`  attributes.

In  `format_string`, you include several formatting codes and all of the dashes (`-`), colons (`:`), and spaces exactly as they appear in  `date_string`. To process the date and time in  `date_string`, you include the following formatting codes:


|Component  |Code  |Value  |
|--|--|--|
|Year (as four-digit integer )  |%Y  |2024  |
|Month (as zero-padded decimal)  |%m  |01  |
|Date (as zero-padded decimal)  |%d  |31  |
|Hour (as zero-padded decimal with 24-hour clock)  |%H  |14  |
|Minute (as zero-padded decimal)  |%M  |43  |
|Second (as zero-padded decimal)  |%S  |37  |

A complete listing of all of the options in the mini-language is outside the scope of this tutorial, but you can find several good references on the web, including in Python’s  [documentation](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)  and on a website called  [strftime.org](https://strftime.org/).

Now that  `date_string`  and  `format_string`  are defined, you can use them to create a  `datetime`  instance. Here’s an example of how  `.strptime()`  works:

```python
 3>>> from datetime import datetime
 4>>> datetime.strptime(date_string, format_string)
 5datetime.datetime(2020, 1, 31, 14, 45, 37)
```
In this code, you import  `datetime`  on  **line 3**  and use  `datetime.strptime()`  with  `date_string`  and  `format_string`  on  **line 4**. Finally,  **line 5**  shows the values of the attributes in the  `datetime`  instance created by  `.strptime()`. You can see that they match the values shown in the table above.

**Note:**  There are more advanced ways to create  `datetime`  instances, but they involve using third-party libraries that must be installed. One particularly neat library is called  [`dateparser`](https://dateparser.readthedocs.io/en/latest/), which allows you to provide natural language string inputs. The input is even supported in a number of languages:

```python
 1>>> import dateparser
 2>>> dateparser.parse("yesterday")
 3datetime.datetime(2020, 3, 13, 14, 39, 1, 350918)
 4>>> dateparser.parse("morgen")
 5datetime.datetime(2020, 3, 15, 14, 39, 7, 314754)
```
In this code, you use  `dateparser`  to create two  `datetime`  instances by passing two different string representations of time. On  **line 1**, you import  `dateparser`. Then, on  **line 2**, you use  `.parse()`  with the argument  `"yesterday"`  to create a  `datetime`  instance twenty-four hours in the past. At the time of writing, this was March 13, 2020, at 2:39 PM.

On  **line 3**, you use  `.parse()`  with the argument  `"morgen"`.  _Morgen_  is the German word for tomorrow, so  `dateparser`  creates a  `datetime`  instance twenty-four hours in the future. At the time of writing, this was March 15 at 2:39 PM.

## Working With Time Zones


The Python  `datetime.tzinfo`  documentation  [recommends](https://docs.python.org/3/library/datetime.html#tzinfo-objects)  using a third-party package called  `dateutil`. You can install  `dateutil`  with  [`pip`](what-is-pip.md):
```shell
$ python  -m  pip  install  python-dateutil
```

Note that the name of the package that you install from PyPI,  `python-dateutil`, is different from the name that you use to import the package, which is just  `dateutil`.


### Using dateutil to Add Time Zones to Python datetime

One reason that  `dateutil`  is so useful is that it includes an interface to the IANA time zone database. This takes the hassle out of assigning time zones to your  `datetime`  instances. Try out this example to see how to set a  `datetime`  instance to have your local time zone:

```python
>>> from dateutil import tz
>>> from datetime import datetime
>>> now = datetime.now(tz=tz.tzlocal())
>>> now
datetime.datetime(2020, 1, 26, 0, 55, 3, 372824, tzinfo=tzlocal())
>>> now.tzname()
'Eastern Standard Time'
```
In this example, you  [import](absolute-vs-relative-imports-python.md)  `tz`  from  `dateutil`  and  `datetime`  from  `datetime`. You then create a  `datetime`  instance set to the current time using  `.now()`.

You also pass the  `tz`  keyword to  `.now()`  and set  `tz`  equal to  `tz.tzlocal()`. In  `dateutil`,  `tz.tzlocal()`  returns a concrete instance of  `datetime.tzinfo`. This means that it can represent all the necessary time zone offset and daylight saving time information that  `datetime`  needs.

You also print the name of the time zone using  `.tzname()`, which prints  `'Eastern Standard Time'`. This is the output for Windows, but on macOS or Linux, your output might read  `'EST'`  if you’re in the US Eastern time zone during the winter.

You can also create time zones that are not the same as the time zone reported by your computer. To do this, you’ll use  `tz.gettz()`  and pass the official  [IANA name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)  for the time zone you’re interested in. Here’s an example of how to use  `tz.gettz()`:

```python
>>> from dateutil import tz
>>> from datetime import datetime
>>> London_tz = tz.gettz("Europe/London")
>>> now = datetime.now(tz=London_tz)
>>> now
datetime.datetime(2020, 1, 26, 6, 14, 53, 513460, tzinfo=tzfile('GB-Eire'))
>>> now.tzname()
'GMT'
```
In this example, you use  `tz.gettz()`  to retrieve the time zone information for London, United Kingdom and store it in  `London_tz`. You then retrieve the current time, setting the time zone to  `London_tz`.

On Windows, this gives the  `tzinfo`  attribute the value  `tzfile('GB-Eire')`. On macOS or Linux, the  `tzinfo`  attribute will look something like  `tzfile('/usr/share/zoneinfo/Europe/London)`, but it might be slightly different depending on where  `dateutil`  pulls the time zone data from.

You also use  `tzname()`  to print the name of the time zone, which is now  `'GMT'`, meaning Greenwich Mean Time. This output is the same on Windows, macOS, and Linux.

In an earlier  [section](python-datetime.md/#creating-python-datetime-instances), you learned that you shouldn’t use  `.utcnow()`  to create a  `datetime`  instance at the current UTC. Now you know how to use  `dateutil.tz`  to supply a time zone to the  `datetime`  instance. Here’s an example modified from the  [recommendation](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow)  in the Python documentation:

```python
>>> from dateutil import tz
>>> from datetime import datetime
>>> datetime.now(tz=tz.UTC)
datetime.datetime(2020, 3, 14, 19, 1, 20, 228415, tzinfo=tzutc())
```
In this code, you use  [`tz.UTC`](https://dateutil.readthedocs.io/en/stable/tz.html#dateutil.tz.dateutil.tz.UTC)  to set the time zone of  `datetime.now()`  to the UTC time zone. This method is recommended over using  `utcnow()`  because  `utcnow()`  returns a  _naive_  `datetime`  instance, whereas the method demonstrated here returns an  _aware_  `datetime`  instance.

Next, you’ll take a small detour to learn about  **naive**  vs  **aware**  `datetime`  instances. 

### Comparing Naive and Aware Python datetime Instances

Python  `datetime`  instances support two types of operation, naive and aware. The basic difference between them is that **naive** instances don’t contain time zone information, whereas **aware** instances do. More formally, to quote the Python documentation:

> An **aware** object represents a specific moment in time that is not open to interpretation. A **naive** object does not contain enough information to unambiguously locate itself relative to other date/time objects. ([Source](https://docs.python.org/3/library/datetime.html#id1))

This is an important distinction for working with Python  `datetime`. An  **aware**  `datetime`  instance can compare itself unambiguously to other aware  `datetime`  instances and will always return the correct time interval when used in arithmetic operations.

**Naive**  `datetime`  instances, on the other hand, may be ambiguous. One example of this ambiguity relates to daylight saving time. Areas that practice daylight saving time turn the clocks forward one hour in the spring and backward one hour in the fall. This typically happens at 2:00 AM local time. In the spring, the hour from 2:00 AM to 2:59 AM  _never happens_, and in the fall, the hour from 1:00 AM to 1:59 AM happens  _twice_!

Practically, what happens is that the offset from UTC in these time zones changes throughout the year. IANA tracks these changes and catalogs them in the different database files that your computer has installed. Using a library like  `dateutil`, which uses the IANA database under the hood, is a great way to make sure that your code properly handles arithmetic with time.


**Note**
Start from Python 3.9 includes a new module called  [`zoneinfo`](https://docs.python.org/3.9/library/zoneinfo.html)  that provides a concrete implementation of  `tzinfo`  that tracks the IANA database, so it includes changes like daylight saving time. However, until Python 3.9 becomes widely used, it probably makes sense to rely on  `dateutil`  if you need to support multiple Python versions.

`dateutil`  also provides several concrete implementations of  `tzinfo`  in the  `tz`  module that you used earlier. You can check out the  [`dateutil.tz`  documentation](https://dateutil.readthedocs.io/en/stable/tz.html)  for more information.


This doesn’t mean that you always need to use **aware** `datetime` instances. But aware instances are crucial if you’re comparing times with each other, especially if you’re comparing times in different parts of the world.

```python
# world_cup_2026_countdown.py

from dateutil import parser, tz
from dateutil.relativedelta import relativedelta
from datetime import datetime

# World Cup 2026 June 11 – July 19 2026
# world_cup_2026_countdown.py

from dateutil import parser, tz
from dateutil.relativedelta import relativedelta
from datetime import datetime

# World Cup 2026 June 11 – July 19 2026
WORLD_CUP_2026_DATE = parser.parse("Jun 11, 2026 10:00 AM")
WORLD_CUP_2026_DATE = WORLD_CUP_2026_DATE.replace(tzinfo=tz.gettz("America/New_York"))
now = datetime.now(tz=tz.tzlocal())

# Countdown to World Cup 2026: relativedelta(years=+5, months=+5, days=+6, hours=+13, minutes=+59, seconds=+59, microseconds=+999999)
countdown = relativedelta(WORLD_CUP_2026_DATE, now)
print(f"Countdown to World Cup 2026: {countdown}")

def time_amount(time_unit: str, countdown: relativedelta) -> str:
    """
    Args:
    time_unit (str): The time unit to be used in the countdown.
    countdown (relativedelta instance): The time difference between two dates.
    """
    t = getattr(countdown, time_unit)
    return f"{t} {time_unit}" if t != 0 else ""

def main():
    now = datetime.now(tz=tz.tzlocal())
    countdown = relativedelta(WORLD_CUP_2026_DATE, now)
    time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
    output = (t for tu in time_units if (t := time_amount(tu, countdown)))
    pycon_date_str = WORLD_CUP_2026_DATE.strftime("%A, %B %d, %Y at %H:%M %p %Z")
    print(f"World Cup 2026 will start on:", pycon_date_str)
    print("Countdown to World Cup 2026:", ", ".join(output))

#countdown = relativedelta(WORLD_CUP_2026_DATE, now)
#time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
#output = (t for tu in time_units if (t := time_amount(tu, countdown)))
#print("Countdown to World Cup 2026:", ", ".join(output))

# Guard clause to make sure that main() only runs when this file is executed as a script.
if __name__ == "__main__":
    main()
```

One neat thing to do might be to allow the user to change the time zone associated with `now` by passing a [command-line argument](command-line-arguments.md). You could also change the `WORLD_CUP_2026_DATE` to something closer to home, say [WORLD_CUP_2030_DATE](https://en.wikipedia.org/wiki/2030_FIFA_World_Cup) or [2024 Summer Olympics](https://www.paris2024.org/en/).



# References
[Using Python datetime to Work With Dates and Times](https://realpython.com/python-datetime/)
[Python strftime cheatsheet](https://strftime.org/)
[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)