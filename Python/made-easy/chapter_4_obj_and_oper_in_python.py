# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     notebook_metadata_filter: -kernelspec
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
# ---

# %%

# %%


"""Chapter 4 Objects and Operators in Python."""


# %%


import keyword
import math

# ## **Variables**

# Variables in Python is just pointers. Technically, variables are just areas in your computer's memory where some information is stored.
#
# Python automatically determines which type of value you assign to a variable.
#
# ***
# **х = 38**
#
# **у = **"emailid@python.com"****
#
# `print(x) `
#
# `print(у)`
#
# ***
#
#
# **print (type (x))**
#
# **print (type (у))**
#
#     `<class 'int'>`
#
#     `<class 'str'>`
# ***
# #### Assignment operator
#
# The sign (=) does not mean "equal". It means "assign" in Python, `"equals" is written as " == "`
#
#
# #### Variable names
#
# Earlier we already spoke about variable names. But let's repeat one more time.
#
# * Variable names can contain only letters, number and underscores.
# * Var names can't be started with numbers. ~~5Finger~~
# * Var names can't contain spaces. ~~sales data~~, correct option is sales_data.
# * Var names are case sensitive. Sales and sales are two different variables.
# * You can't use reserved names such as: any, break, try and etc.
# * Hint: to check reserved words you can execute this code:

# %%


print(keyword.kwlist)


# ## Program Structure
#
# Before moving forward, let's take a look to the hierarchical structure of the program.
#
# In Python we highlight such parts as: modules, expressions, operators and objects.
#
# * The programs consist of modules.
# * Modules contain expressions.
# * Expressions contain operators.
# * Operators create and process objects.
#
# So, modules are at the top of the program hierarchy, and objects make up it the basis.
#

# ### Objects
#
# We perform operations on Objects.
#
# Examples of simple operations are addition, multiplication of Numbers(Objects) or concatenation of strings (Objects).
#
#
# In Python, all data becomes objects. Objects can either be embedded, which are in Python natively, or we create them ourselves using classes
# Python.
#
# We will also see that in Python everything is an object, whether it's prime numbers or operations performed on them. For a Python script, all these things are objects. Python supports OOP, i.e. object-oriented programming.

#
#
# ***
# #### Classification of Objects
#
# 1. Built-in Objects.
# 2. User-defined objects
#
#     Can also be classified as:
#
#     1. Mutable Objects
#     2. Immutable Objects
#
#
#
# ***
#
#
# | Object type | Example of Objects | Mutable or Immutable |
# |-------------|--------------------|----------------------|
# | Number      | 1234, 3 .1415, 3+4j , OЫll, Decimal (), Fraction ()| Immutable |
# | String | ' nilabh', "Bob's" | Immutable
# | List | [ 1, [ 2, ' three ' ] , 4 . 5] , list ( range (lO) ) | Mutable
# | Dictionary | { ' food' : ' spam' , ' taste ' : ' yum' }, dict (hours:10) | Mutable
# | Tuples | ( 1, ' spam' , 4, 'U' ) , tuple (' spam' ) | Immutable
# | Sets | set ( ' аЬс' ) , { ' а', 'Ь', ' с ' } | Mutable
# | Logical | 0, 1 | Immutable
# | Program components | functions, modules, classes |
#
#
#
#
#
#
#

# #### Object's Identity, values, and types
#
#
# Objects are Python's abstraction for data.
#
# Any data in a Python program is represented either by objects or by relations between objects.
#
# You may think of an Object, as a combination of 3 things:
# * Identity Type
# * Type
# * Value
#
# An object's identity never changes once it has been created. That becomes the object's address in memory.In Python, every Object’s Identity (or Address in memory) is represented by a number. You can see that number by using the id() function.

# %%


a_id_example: int = 5
id(a_id_example)


# The type() function returns an object's type. Like its identity, an object's type is also unchangeable.

# %%


str  # str means String.


# %%


float  # floating point number


# %%


type(["x", "yz", "abc"])  # list containing 3 strings


# %%


type(["x", "y", 1])  # list containing 2 strings and one number


# %%


type({"food": "spam", "taste": "yum"})  # dictionary


# ### Mutable and Immutable Objects
#
# The value of some objects can change. Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable.
#
#
# * instance, numbers, strings, and tuples are immutable
# * dictionaries and lists are mutable
#
#
# Some objects contain references to other objects; these are called `containers`. Examples of containers are **tuples**, **lists**, and **dictionaries**.
#
#

# #### The standard type hierarchy
#
#
# Below is a list of the types that are built into Python.
#
# ##### Built-in constants
#
# 1. None - this type has a single value. This object is accessed through the built-in name `None`.  it is returned
# from functions that don't explicitly return anything. Its truth value is false.
#
# 2. NotImplemented - this type has a single value. There is a single object with this value. This object is accessed through the built-in name NotImplemented. Its truth value is true.
#
# 3. Ellipsis - this type has a single value. There is a single object with this value. This object is accessed through the literal ... or the built-in name Ellipsis. Its truth value is true
#
#
#

# #### Numeric types
#
# These are created by numeric literals and returned as results by
# arithmetic operators and arithmetic built-in functions. Numeric
# objects are immutable; once created their value never changes.
#
# 1. `Integers (int)` - these represent numbers in an unlimited range, subject to available (virtual) memory only.
#
# 2. `Booleans (bool)` - these represent the truth values False and True. The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1.
#
# 3. `Real numbers (float)` - these represent machine-level double precision floating point numbers.
#
# 4. `Complex numbers (complex)` - These represent complex numbers as a pair of machine-level double precision floating point numbers. The same caveats apply as for floating point numbers. The real and imaginary parts of a complex number z can be retrieved through the read-only attributes z.real and z.imag.
#
#

# #### Sequences
#
# These represent finite ordered sets indexed by non-negative
# numbers. The built-in function `len()` returns the number of items of a sequence.  Item i of sequence a is selected by a[i]
#
# Sequences are distinguished according to their mutability.
#

# #### Immutable sequences
#
# Immutable sequences - An object of an immutable sequence type cannot change once it is created.The following types are immutable sequences:

# ##### Strings
#
# A string is a sequence of values that represent Unicode code points.
#
# Python doesn't have a char type; instead, every code point in the string is represented as a string object with length 1.
#
# All the code points in the range U+0000 - U+10FFFF can be represented in a string.
#
# The built-in function `ord()` converts a code point from its string form to an integer in the range 0 - 10FFFF;
#
# `chr()` converts an integer in the range 0 - 10FFFF to the corresponding length 1 string object.

# %%


ord("nilabh"[3])  # this is same as ord('a')


# %%


ord("a")


# %%


chr(97)


# %%


print(chr(96))
print(chr(100))
print(chr(99))
print(chr(1045))
print(chr(100009))


# ##### Tuples
#
# The items of a tuple are arbitrary Python objects. Tuples of two or more items are formed by comma-separated lists of expressions. An empty tuple can be formed by an empty pair of parentheses. `('xyz', 5, 'p') is an example of a tuple.`

# #### Bytes
#
# A bytes object is an immutable array. The items are 8-bit bytes,
# represented by integers in the range 0 <= x < 256. Bytes literals (like b'abc') and the built-in bytes() constructor can be used to create bytes objects. Also, bytes objects can be decoded to strings via the decode() method.
#

# #### Mutable sequences
#
# Mutable sequences can be changed after they are created. There are currently two intrinsic mutable sequence types:
#

# #### Lists
#
# The items of a list are arbitrary Python objects. Lists are formed by placing a comma-separated list of expressions in square brackets.
#
# ['xyz', 5, 'p'] is an example of a list.
#

# ##### Byte Arrays
#
# A bytearray object is a mutable array. They are created by the built-in bytearray() constructor.

# #### Set types
#
# These represent unordered, finite sets of unique, immutable objects.
#
# Common uses for sets are fast membership testing, removing
# duplicates from a sequence, and computing mathematical operations
# such as intersection, union, difference, and symmetric difference.
#
# ##### Sets
#
# These represent a mutable set. They are created by the built-in set() constructor and can be modified afterward by several methods, such
#
# {"apple", "banana", "cherry"} is an example of a set
#
# ##### Frozen sets
#
# These represent an immutable set. They are created by the built-in
# frozenset() constructor. As a frozenset is immutable and hashable, it can be used again as an element of another set, or as a dictionary key.
#
#
#
#

# #### Mappings
#
# These represent finite sets of objects indexed by arbitrary index sets. The subscript notation a[k] selects the item indexed by k from the mapping a; this can be used in expressions and as the target of assignments or del statements. The built-in function len() returns the number of items in a mapping.
#
#
# ##### Dictionaries
#
# These represent finite sets of objects indexed by nearly arbitrary values. The only types of values not acceptable as
# keys are values containing lists or dictionaries.
#
# Dictionaries are mutable; they can be created by the `{...} `notation
#
# `{"brand": "Ford", "model": "Mustang", "year": 1964}` is an example of a dictionary in python

# #### Callable types
#
# These are the types to which the function call operation can be
# applied:
#
# ##### Built-in functions
#
# A function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. Examples of built-in functions are `len()` and `math.sin()` (math is a standard built-in module)
#
# **To call a function, use the function name followed by a parenthesis.**
#
#
# ##### Instance methods
#
# An instance method object combines a class, a class instance, and any callable object (normally a user-defined function)
#
# ##### Built-in methods
#
# Python method is like a function, except it is attached to an object An example of a built-in method is `alist.append()`, assuming alist is a list object.
#
# ##### Classes
#
# Classes are callable. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made.
#
#
#
#
#
#
#

# #### Modules
#
# Consider a module to be the same as a code library. To create a
# module just save the code you want in a file with the file extension `.py` Now we can use the module we just created, by using the import statement.
#
# Modules are a basic organizational unit of Python code and are created by the import system as invoked either by the import statement or by calling functions such as importlib.import_module() and built-in import().
#
#

# ### Operators
#
# Assignment Operators
#
# | Operator | Operation | Equivalent |
# |----------|-----------|------------|
# | =       | a = b| a = b |
# | += | a += b  | a = (a + b) |
# | -= | a -= b | a = (a - b) |
# | *= | a *= b | a = (a * b) |
# | /= | a /= b | a = (a / b) |
# | %= | a %= b | a = (a % b) |
# | //= | a //= b | a = (a // b) |
# | **= | a **= b | a = (a ** b) |
#

# Comparison Operators
#
# | Operator | Operation |
# |----------|-----------|
# | ==       | Equality|
# | != | Inequality |
# | > | Greater than |
# | < | Less than |
# | >= | Greater than or equal to |
# | <= | Less than or equal to |

# Logical Operators
#
# | Operator | Operation |
# |----------|-----------|
# | and       | Logical AND|
# | or | Logical OR |
# | not | Logical NOT |
#
#

# Conditional Operator
#
# | Operator | Operation |  |
# |----------|-----------|------------|
# | Identity Operator | | |
# | is | x is y  | True if x and y are same objects |
# | is not | x is not y | True if x and y are not the same objects |
# | Membership Operator |  |  |
# | in | x in y | True if x is a member of collection y |
# | not in | x not in y | True if x is a not a member of collection y |
#

# %%


4 == 2 * 2


# %%


input_string: str = "string"
if "i" in input_string:
    print("True, Found 'i' in the string")


# #### Indentation
#
# One of the most unmistakable highlights of Python is its utilization of Indentation to mark Blocks of Code.
#
# In Python, it is used for indicating what block of code a
# statement belongs to.
#
# Incorrect indentation will result into `IndentationError`

# #### Python Comments
#
# Comments are very useful while writing a program. It makes the code more readable and tells what's going on inside a program so that a person looking at the source code does not have a hard time figuring it out.
#
# In Python, we use the hash (#) symbol to begin the writing of a
# comment.
#
# Python Interpreter ignores the comment

# #### Order of Evaluation in Python
#
# You would remember the order of evaluation in a mathematical
# equation. Similarly, Python has its own `Operator precedence`.
#
#
# The following table summarizes the operator precedence in Python,
# from lowest precedence (least binding) to highest precedence (most binding).
#
#
# | Operator | Description |
# |----------|-----------|
# | lambda   | Lambda expression |
# | if-else | Conditional expression |
# | or | Boolean OR |
# | and | Boolean AND |
# | not x | Boolean NOT |
# | in, not in, is, is not, <, <=, >, >=, !=, ==| Comparisons including membership tests and identity tests |
# | ^ | Bitwise XOR |
# | & | Bitwise AND |
# | <<, >>  | Shifts |
# | +, -  | Addition and subtraction |
# | *, @, /, //, %  |  Multiplication, matrix multiplication, division, floor, division, remainder |
# | +x, -x, ~x | Positive, negative, bitwise NOT |
# | ** | Exponentiation |
# | await x  | Await expression |
# | x[index], x[index:index], x(arguments...), x.attribute | Subscription, slicing, call, attribute reference
# | (expressions...), [expressions...], {key: value...}, {expressions...} | Binding or tuple display, list display, dictionary display, set |display
#
#
#

# #### Changing the Order of Evaluation
#
# To make the expressions more readable, we shall use parentheses. For example, 2 + (3 * 4) is definitely easier to understand than 2 + 3 * 4 which requires knowledge of the operator precedence.

# #### Dynamic Typing
#
# In Python, though the value that a variable point to has a type, the variable itself has no strict type in its definition. You can reuse the same variable to point to an object of a different type.

# %%


six_number: int = 6
six_number


# %%


six_string: str = "six"
six_string


# #### Summary
#
# In this chapter, we learned the Semantics of Python as a language, and also brushed some of the Syntax or python we saw in the previous chapter. We learned about the hierarchy and
# structure of Python code. How everything is an Object in Python, and what are the features of objects. We have seen how to use operators, operands, and expressions - these are the basic building blocks of any program.

# #### Answer the following
#
# 1. **What is a Variable in Python? How is it different from an object?**
#
#     Variables in python are just pointers. They do not have any value in themselves, but they point to the object they are assigned to.
#
#     An object is a data structure in Python, representing any value (like numbers, strings, lists, etc.). Everything in Python is an object, including functions and classes.
#
#
# 2. **What is the convention to name a variable in Python?**
#
#     * Variable names can contain only letters, number and underscores.
#     * Var names can't be started with numbers. ~~5Finger~~
#     * Var names can't contain spaces. ~~sales data~~, correct option is sales_data.
#     * Var names are case sensitive. Sales and sales are two different variables.
#     * You can't use reserved names such as: any, break, try and etc.
#
# 3. **What are the advantages of having built-in objects in Python?**
#
#     Built-in objects making easier to perform common tasks without requiring custom implementations
#
# 4. **What does immutable means? What objects are immutable in Python?**
#
#     Objects whose value can change are said to be mutable.
#
#     Objects whose value is unchangeable once they are created are called immutable
#
# 5. **What do you mean by an object's Identity? How is it different from its type?**
#
#     Object's identity refers to its unique location in memory.
#
#     Type defines what kind of object it is and what behavior (methods, operations) it supports.
#
# 6. **What do chr() and ord() functions do? How are they related to one another?**
#
#     The chr() and ord() functions in Python are used for converting between characters and their corresponding Unicode (or ASCII) integer values.
#
#     chr() - `converts an integer `(Unicode code point) into the corresponding character.
#
#     ord() - `converts a character` into its corresponding Unicode (or ASCII) integer value.
#
# 7. **What is an operator? How many types of Operators are there in Python? Name them all.**
#
#     An operator in Python is a symbol that performs an operation on one or more operands (values or variables)
#
#     Arithmetic Operators
#     Comparison Operators
#     Conditional Operator
#     Logical Operators
#     Identity Operators
#     Bitwise Operators
#     Membership Operators
#
# 8. **/ And //, both are division operators. What is the difference between them?**
#
#     / - floating-point division, always returns a floating-point number
#     // - floor division, Divide x by y and round the answer down to the nearest integer value. If one of the values is a float you'll get back a float
#
# 9. **What value do the logical operators return?**
#
#     These operators are used to perform logical operations, and they return either a boolean value (True or False)
#
# 10. **What is the importance of Indentation in Python Programming language?**
#
#     Indentation is used to define the structure of the program by grouping statements into blocks.
#
# 11. **How do you write comments in Python? Why are they important**
#
#     Comments are used to add explanatory notes or descriptions within the code
#
#     They help programmers and others reading the code understand its purpose and functionality
#
#     You can write a single-line comment by placing a hash symbol # before the comment text.
#
# 12. **How to change the order of evaluation in Python**
#
#     The most common way to change the order of evaluation in Python is to use parentheses ()
#
# 13. **What is the difference between a logical line and a physical line?**
#
#     A physical line refers to a single line of text in the source code file.
#
#     A logical line is a unit of code that Python interprets as a single statement or command, regardless of how many physical lines it spans.
#
#     **Example with multiple physical lines forming a single logical line**
#
#
#     * result = (1 + 2 +
#
#             3 + 4)  This is one logical line split across multiple physical lines
#
#
#
#

# #### True or False
#
# 1. Variables in Python acquire the value assigned to them.
#
#     True
#
# 2. In Python, before creating a variable, you need to define its  type first.
#
#     False
#
# 3. x = 38 and x == 38 are not the same thing in Python.
#
#     True
#
# 4. We perform operations on objects in Python.
#
#     True
#
# 5. Python Keywords can be used as the name of a variable.
#
#     False
#
# 6. Custom data structures are more efficient than the built-in objects.
#
#     False
#
# 7. An object's identity never changes once it’s created.
#
#     True
#
# 8. Comments in programs make the program more readable and easy to
# understand.
#
#     True
#
# 9. Indentation is just a way to make programs better looking and more readable.
#
#     False
#
# 10. The % (Modulo) operator is used to find out if the division of two numbers yields any remainder.
#
#     True

# #### Write your own Codes for this

# 1. Peter's salary is 12000 per month. If he saves 20% of his salary every month, write a code to calculate his total savings at the end of the year.
#

# %%


salary: int = 12000

savings_per_month: float = salary * 0.2

total_savings: float = savings_per_month * 12

total_savings


# 2. Distance between Mumbai and Delhi is 1422 KMs. If Sundar travels in a car with an average speed of 45 Miles per hour, how long will it take him to cover this distance?

# %%


city_distance: int = 1422  # kms

car_speed: int = 45  # mph

car_speed_kms: float = car_speed * 1.60934

cover_time: float = city_distance / car_speed_kms

cover_time


# 3. The temperature of a normal person is in the range of 97 degrees
# Fahrenheit to 99 degrees Fahrenheit. What will be this range in
# Degree Centigrade?

# %%


def fahrenheit_converter(fahrenheit: float) -> float:
    """Convert a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in degrees Fahrenheit.

    Returns:
        float: The temperature converted to degrees Celsius.
    """
    return (5 / 9) * (fahrenheit - 32)


fahrenheit_low: int = 97
fahrenheit_high: int = 99


temp_celsius_low: float = fahrenheit_converter(fahrenheit_low)
temp_celsius_high: float = fahrenheit_converter(fahrenheit_high)


print(f"{temp_celsius_low:.2f}°C to {temp_celsius_high:.2f}°C")


# 4. Take any 6 digit number. Write a program to calculate the sum of all
# the digits of the numb

# %%


def sum_of_digits(number: int) -> int:
    """Calculate the sum of all digits in a given number.

    Args:
        number (int): The number whose digits are to be summed.

    Returns:
        int: The sum of the digits of the input number.
    """
    return sum(map(int, str(number)))


six_digit_number = 123456
result = sum_of_digits(six_digit_number)

result


# 5. Sales per month of 5 Book Shops in Brooklyn, New York City are as follows. A = $6500, B = $8000, C = $12000, D = $4900 and E = $5600. Assuming that there are only these 5 book shops in Brooklyn, find out the market share of each shop. Also notice, what is the sum of the market share of all the shops? (Market share means, the share of one)
#

# %%


shop_dict: dict[str, int] = {
    "A": 6500,
    "B": 8000,
    "C": 12000,
    "D": 4900,
    "E": 5600,
}

for shop, sales in shop_dict.items():
    print(shop, sales / (sum(shop_dict.values()) - sales))


# 6. John buys a mobile phone for 1800 from Kolkata and sells it at Mumbai at a gain of 25%. If his overhead expenses are 5% of the selling price, then what is his selling price?

# %%


phone_price: int = 1800

phone_margin: float = phone_price * 1.25

selling_price: float = phone_margin * 0.95

selling_price


# 7. Find the volume and Surface area of a cube whose diagonal is 5 Mtr

# %%


diagonal: int = 5

cube_volume = diagonal**3 / math.sqrt(3)
cube_surface = 2 * (diagonal**2)

print(cube_volume, cube_surface)


# 8. Three cubes of metal whose edges are 3, 4, and 5 cms respectively, are melted and formed into a single cube. Find the edge of the new cube formed.

# %%


first_edge: int = 3
second_edge: int = 4
third_edge: int = 5


volume_one: float = first_edge**3
volume_two: float = second_edge**3
volume_three: float = third_edge**3


total_volume: float = volume_one + volume_two + volume_three


new_edge: float = total_volume ** (1 / 3)

new_edge


# 9. Write a 6 digit number. Write a program to reverse the order of the digits in the number

# %%


six_digit_number = 123456
reversed_digits = int(str(six_digit_number)[::-1])
reversed_digits
