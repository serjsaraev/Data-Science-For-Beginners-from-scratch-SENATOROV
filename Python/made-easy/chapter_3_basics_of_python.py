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


"""Chapter 3 Python Basics."""


# ## Python

# ### **| Numbers |**

# * Lets start to learn computer programming with "Hello world!".
# * Simply write down `print("Hello World ! ")` in a new cell.

# * Let's move on and try to write some commands and see the result.
# * The Python interpreter can be used as a simple calculator

# * print("Result of 2 + 2 is:", 2 + 2)
# * print("Result of 50-5*6 is:", 50 - 5 * 6)
# * print("Result of 8/5 is:", 8 / 5)

# * Integers are - `int` type.
# * Numbers with a fractional part have a `float` type.
# * **The division operator / always returns float.**

# * print("Result of 17 // 3 is: ", 17 // 3)  # integer division
# * print("Result of 17 % 3 is: ", 17 % 3)  # the remainder of the division
# * print("Result of 5 ** 2 is: ", 5**2)  #  ** operator to calculate the degree.

# **The equal sign `=` is used to assign a value to a variable.**

# * width = 20
# * height = 5 * 8
# * my_name = "Chyngyz"

# ### **| Strings |**

# * Python can work with strings which can be set in a few ways. `'....'` or `"...."` will print same result.
# * A string is enclosed in double quotes if it contains single quotes and does not contain double quotes
# * Otherwise the string is enclosed in single quotes
#

# %%


# print("'Isn't', they said")
# print("C :\\some\name ")  # here \n is a transition to a new line!
# print(r"C: \some\name ")  # r before the opening quotation mark


# * Strings can be combined.
# * The `+` operator **adds up**, and the operator `*` **multiplies**.

# %%


# print("a" + "b")
# print("t" * 5)
# print("no" * 3 + "dip")


# * Two strings that are located next to each other, are automatically combined.
# * This is especially useful if you need to split long strings.

# %%


# text = " Put several strings within parentheses -" "
# - to have them joined together. "
# text


# ### **| Indexing |**

# * Strings can be indexed (access the elements of the string by index).
# * Index of first element is `0`.

# %%


# word = "Python"
# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])
# print(word[5])
#
#
# print(word[-4])  # For negative indices, the countdown is on the right


# ### **| Slicing |**

# The slice returns a substring. Note that the initial index is always included, and the final one is always excluded.

# %%


# print(word[:2] + word[2:])


# Python strings cannot be changed - they are immutable. Therefore, it is not possible to assign a new value to a symbol by a specific index.

# %%


# print(len(word))  #  function len returns string's length


# ## Python Code Syntax
# ### **| Expressions |**

# * The strings written in the source code for execution are called `expressions.`
#
# * For example, n = 20 is an expression with an assignment operator.
#
# * Multiline extensions can be transferred to other lines using parentheses

# %%


# moving an expression to a new line using \
# s = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
# print(s)

# moving an expression to a new line using ()
# n = 1 * 2 * 3 + 7 + 8 + 9
# print(n)

# moving an expression to a new line using []
# footballer = ["Messi", "Neymar", "Suarez"]
# print(footballer)

# moving an expression to a new line using {}
# x = {1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9}


# %%


# You can also end an expression with a semicolon (;)
# flag = 2
# ropes = 3
# pole = 4
#
# print(flag, ropes, pole)


# * For variables, you should choose names with meaning that say something about the stored data.
#
# * Variables could be any length and contain letters and numbers.
#
# * Python is case sensitive, so be careful. Same name with different case are different.
#
#
# * **Here are some rules for variable naming:**
#
# 1. Variable name should start with letter!
# 2. You can't use space!
# 3. For long names you can use the underscore character (_)!
# 4. Python keywords cannot be used as variable names:
#
#
# * `and`      `def`    `exec`     `if`      `not`   `return`
# * `assert`   `del`    `finally`  `import`  `or`    `try`
# * `break`    `elif`   `for`      `in`      `pass`  `while`
# * `class`    `else`   `from`     `is`      `print` `yield`
# * `continue` `except` `global`   `lambda`  `raise`

# ### **| First steps |**

# We can use Python for more complex tasks, Let's try to calculate the beginning of the Fibonacci series
# as follows:

# * a: int = 0
# * b: int = 1
# * while a < 10:
#     * print(a)
#     * a, b = b, a + b
#
# * 0
# * 1
# * 1
# * 2
# * 3
# * 5
# * 8

# Let's experiment with this simple code. First, let's change the way variables a and b are assigned.

# * a, b = 0, 1
# * while a < 15:
#     * print(a)
#     * a, b = b, a + b
#
#
#
# * 0
# * 1
# * 1
# * 2
# * 3
# * 5
# * 8
# * 13

# * Let's look at a couple important concepts using print() function as example.
#
# * The actual syntax of the print() function looks like this:
#
# * **`print ( *objects, sep= ' ', end= ' \n', file=sys.stdout, flush=False)`**
#
# * Using this syntax as an example, let's look at `two more important concepts` of programming in Python:
#
#     1. Arguments (args).
#     2. Named arguments (kwargs).
#
#

# #### Arguments
#
# Arguments are all that we give to the function.
# If you want to pass more than one variable to a function when defining it, but don't know yet exactly how many arguments you will have, you can specify a special syntax *args. The * symbol here means that we can pass any number of variables to the function, and the word `args` is a kind of standard convention that is used for better code readability. You can use any other layer, if it is significant enough. As you can see, the syntax of the print() function uses the word *objects instead of *args.

# #### Named arguments
#
# Named arguments are arguments for which, when passed to a function, not only the value is specified, but also the name.
#
# Let's take an example of print() function:
#
# * `*objects` - any number of any objects. Before output all objects are assembled into a string.
# * `sep = ' ' (optional)` - sets the object separator, if there are several of them. Default value - 'space sign'
# * `end = '\n' (optional)` - defines what to output at the end of string. Default value - '\n' - line break sign
# * `file = sys.stdout` (optional) - an object with the write (string) method. If this parameter is not specified, `sys.stdout` will be used by default, which means
# that the results are displayed on the screen.
# * `flush=False (optional)` - a boolean value indicating whether the output will be cleared or buffered (False). `The default value is False.`
#
#

# %%


# Little tricks, what you can do with print function

# name = "Chyngyz"
# last_name = "Mirzamatov"
# place = "Chicago"
#
# print("{} {} lives in {}".format(name, last_name, place))


# ### Finding errors
#
# We have to resort to error detection in cases, our code does not give the desired
# result or does not output anything at all.
#
# There are three types of errors that occur often.
#
# * Syntax error - problems with language constructions.
# * Runtime error - problems with code execution.
# * Semantic error - is an unexpected result

# ##### Syntax errors
#
# The error occurs when you write code without following the Python syntax.
#
# `SyntaxError : invalid syntax `
#
# ##### Runtime error
#
# Runtime errors occur while the program is running. Because Python is an interpreted language, such errors occur only at the moment when the execution of the program reaches an erroneous line.
#
# The common reasons for such errors are as follows:
#
#  * The name of a variable or function entered incorrectly;
#  * Using a variable before defining it;
#  * The name should have been enclosed in quotation marks;
#  * Division by zero.
#
# `ZeroDivisionError : division Ьу zero `
#
#
# A runtime error occurs when Python understands the command itself, but encounters problems when executing it. That's why this error is called "runtime", because it occurs only after the program is started.
#
#
# ##### Semantic error
#
#
# Semantic or logical errors are problems with the very construction of your program. Usually such problems do not cause error messages, but the behavior of the program turns out to be incorrect
#
# `Semantic errors are the most difficult to eliminate.`
#

# #### Exercises
#
#
# ##### Answer the questions:
#
# 1. Questions:
# * ' + '- add operator
# * ' - ' - sub operator
# * ' * ' - multiply operator
# * ' : ' - division operator
#
# 2. " ** " operator to calculate the degree, " * " multiply operator
#
# 3. The strings written in the source code for execution are called `expressions.`
#
# 4. Variables are used to store data. To assign variable we can use operator ' = '
#
# 5. We can't name variable as 'import' because this Python keywords.
#
# 6. Python is case sensitive, so only math is correct option.
#
# 7. You can use brackets to group expressions
#
# 8.  When you write code without following the Python syntax is syntax error. Semantic error - behavior of the program is incorrect.
#
# 9. Default values for: sep - space sign, end - line break sign.
#
#
# ##### False or True
#
# 1. False
# 2. True
# 3. True
# 4. False
# 5. False
# 6. False
# 7. False
# 8. True
# 9. False
# 10. True
#

# %%


friends_name: str = "Daniel"
friends_last_name: str = "Santos"

print(friends_name + " " + friends_last_name)


# %%


l_: int = 23
h_: int = 8
p_: int = l_ * h_
print("Rectangle length is:", p_)


# %%


square: int = 32**2
cube: int = 27**3

print("square of 32 is:", square, "cube of 27 is:", cube)


# %%


a_: int = 2
b_: int = 4
(a_ + b_) ** 2 == a_**2 + b_**2 + 2 * a_ * b_


# %%


name_len: str = "Chyngyz"

print("my name's length is", len(name_len))


# %%


print("__________")
print("|        |")
print("|        |")
print("|        |")
print("|        |")
print("|        |")
print("|        |")
print("|        |")
print("----------")


# %%


print("________")
print("|       |")
print("|       |")
print("|_______|")
print("|")
print("|")
print("|")


# %%


Name: str = "Chyngyz"
Age: int = 23
print(f"My name is {Name}, my age - {Age}")


# %%


words = ["cat", "window", "defenestrate"]
for w_ in words:
    print(w_, len(w_))


# %%


c_, d_ = 0, 1
while c_ < 15:
    print(c_, end=" , ")
    c_, d_ = d_, c_ + d_
