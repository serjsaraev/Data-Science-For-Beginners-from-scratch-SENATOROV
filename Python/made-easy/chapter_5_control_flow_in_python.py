# +


"""Chapter 5 Control Flow Statement."""


# # Control Flow Statement

# Control Flow Tools - code execute in the order in which it was written.
#
# What if we want to change or alter the flow?
#
#

# ![Control-Flow-Tool](img/control_flow.png)
#

# ### IF Operator
#
#
# If condition followed by a colon. The code block of `if` statement comes in the next line, and it must be `indented`. The indentation tells python, that this block of code is for the if statement.
#
# `if condition:`
# * ` do work`
#
# `end if`
#
# The last line, end if is not written. The statement ends itself. You will see that in the example coming below

# ![if-statement-flow-chart](img/if_statement_chart.png)

# ### IF-Else
#
# The if statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block).
#

# ### IF – Elif – Else
#
# Statement It's evident from the name itself, elif is combination of else and if.

# ![if-elif-flow-chart](img/if_elif.png)

# There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation.
#
# The elif and else statements must also have a colon at the end of
# the logical line followed by their corresponding block of statements.
#
# You can have another if statement inside the if-block of an if statement and so on - this is called a nested if statement.
#

# ### For (loop) operator
#
#
# The for statement in Python iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.
#
# `Iteration means the repetition of a process or utterance.`

# ![for-loop-chart](img/for_loop.png)

# +


words: list[str] = ["cat", "window", "defenestrate"]

for w_ in words:
    print(w_, len(w_))


# Here, in the statement, for w in words: , w is just a notation, and doesn't have a meaning of the original alphabet. What it means is, you
# may write, anything there.
#
# So it is essentially
#
# for **`variable`** in **`sequence`**: take action
#

# ### For loop with else
#
# A for loop can have an optional else block as well. The else part is  executed when the items in the sequence used in for loop exhausts.

# ![for-loop-chart](img/for_else.png)

# +


numbers: list[int] = [1, 2, 3, 4, 5]

for i in numbers:
    print(i)

print("this is end of the code")


# ### The `range()` Function
#
#
# If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions

# +


for i in range(5):
    print(i)


# The given endpoint is never part of the generated sequence. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’)
#
# * range(5, 10) 5, 6, 7, 8, 9
# * range(0, 10, 3) 0, 3, 6, 9
# * range(-10, -100, -30) -10, -40, -70
#
#
# To iterate over the indices of a sequence, you can combine range()
# and len() as follows:
#

# +


names: list[str] = ["Mary", "Tom", "Chris", "Charles"]

for i, name in enumerate(names):
    print(i, name)


# ### While Loop
#
# The while loop is used to iterate over a block of code as long as the condition is true.The while loop is used `when we do not know how many times to iterate`.

# ![while-loop](img/while_loop.png)

# +


n_: int = 10

total_sum: int = 0

i_: int = 1

while i_ <= n_:
    total_sum = total_sum + i_
    i_ = i_ + 1
print("The sum is", sum)


# As long as the condition of while returns "True", the loop will run. And when it’s over, it goes to the next statement, which is print. The value of the counter variable needs to increase in the body of the loop. This is very important (and mostly forgotten). Failing to do so will result in an infinite loop (never-ending loop).
#
#
# Similar to the for loop, else block can optionally be used with while
# loop also. The usage is the same as for the for loop
#
#

# ### Break and Continue
#
#
# #### Break Statement
#
# The break statement breaks out of the innermost enclosing for or while loop. it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.
#

# +


list_number = [1, 2, 3, 4, 5]

for i in list_number:
    print(i)
    break
else:
    print("this is end of the code ! ")

print("this line is outside the loop")


# +


for n_ in range(2, 10):
    for x_ in range(2, n_):
        if n_ % x_ == 0:
            print(n_, " equals ", x_, "*", n_ // x_)
            break
    else:
        print(n_, "is а prime numЬer ")


# #### Continue Operator
#
# The continue statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues with the next iteration.

# ![while-loop](img/continue_statement.png)

# +


for alphabet in "python":
    if alphabet == "t":
        continue
    print(alphabet)
print("The end")


# +


for num in range(2, 10):
    if num % 2 == 0:  # четное число
        print("Found an even nшnЬer", num)
        continue
    print("Found а nшnЬer", num)


# ### Pass Operator
#
# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action
#
# This is commonly used for creating minimal classes:
# * class MyEmptyClass: pass
#
#
# Another place pass can be used is as a place-holder for a function or
# conditional body when you are working on a new code, allowing you to
# keep thinking at a more abstract level. The pass is silently ignored:
#
# * def initlog(*args): pass

# ### Summary
#
# In this chapter we learned how to control the flow of the code. Without the if statements or the loops, the codes can be only one directional. We saw how to break a loop, or how to conditionally continue the loop without falling out.

# ## Exercises:
#
# 1. Code execute in the order in which it was written
#
# ### True or False?
#
# 1. False
# 2. True
# 3. False
# 4. True
# 5. True
# 6. True
# 7. True
# 8. True
# 9. False
# 10. True
#

# 1. A trader wants a program to check whether he made a profit or loss over a trade. Write the program where the input for buying and selling price is entered through keyboard input, and the program tells if the trader made a profit or loss. The program shall also calculate the profit or loss made.

# +


buy_price: float = float(input("Buy price"))
sell_price: float = float(input("Sell price"))

margin: float = sell_price - buy_price

if margin > 0:
    print(f"Your profit is {margin}")
elif margin < 0:
    print(f"Your loss is {abs(margin):.2f}")
else:
    print("Sorry no profit for you :(")


# 2. Write a program to check whether the year entered through the keyboard is a leap year or not

# +


current_year: int = int(input("What's current year?"))

if current_year % 4 == 0 and current_year % 100 != 0:
    print("This is leap year")
else:
    print("Not a leap year")


# 3. Three employees Sameer, Pravin, and Mohit enter their years of experience through keyboard input. Write a program to determine the most and the least experienced among the three.
#
#

# +


sameer_exp: int = int(input("What is your experience, Sameer?"))
pravin_exp: int = int(input("What is your experience, Pravin"))
mohit_exp: int = int(input("What is your experience, Mohit?"))

if sameer_exp > pravin_exp and sameer_exp > mohit_exp:
    print("Sameer is most experienced")
elif pravin_exp > sameer_exp and pravin_exp > mohit_exp:
    print("Pravin is most experienced")
else:
    print("Mohit is most experienced")


# 4. A Sum of three angles inside a triangle is 180 degrees. Write a program to check if the shape is a triangle or not, when the three angles are given as input.
#

# +


first_angle: int = int(input("Write first angle"))
second_angle: int = int(input("Write second angle"))
third_angle: int = int(input("Write third angle"))

sum_of_angle: float = first_angle + second_angle + third_angle

if sum_of_angle == 180:
    print("It's triangle")
else:
    print("It's not triangle")


# 5. When the three angles of a triangle are given, write a program to check if its a right angle triangle or not. (One angle must be 90 degrees)

# +


angle_list = [first_angle, second_angle, third_angle]
is_right_angle = False

for i in angle_list:
    if i == 90:
        is_right_angle = True
        break

if is_right_angle:
    print("It's a right angle triangle.")
else:
    print("It's not a right angle triangle.")


# 6. Write the code to output multiplication table of any number given as input.
#

# +


multiply_number: int = int(input("Write your number to display multi table"))
for i in range(1, 11):
    result = multiply_number * i
    print(f"{multiply_number} x {i} = {result}")


# 7. Write a program to print all prime numbers between 1 to 500

# +


for i in range(1, 501):
    if i % 2 != 0:
        print(i)


# 8. Print all the multiples of 9, which are less than 300

# +


for i in range(1, 301):
    if i % 9 == 0:
        print(i)


# 9. A machine gives annual earning of Rs 2000 during its lifetime. It costs Rs.10000 and can be sold off for Rs. 2500 when it is discarded. If 8 percent per annum can be earned if the same amount is invested in some alternate investment, what would be the minimum life of the machine to make it a more attractive investment compared to alternative investment?

# +


car_price: int = 1000000
resale_price: int = 250000
annual_income: int = 200000
rate: float = 0.08
n_value: int = 0

while True:

    car_income: int = annual_income * n_value + resale_price

    investment_income: float = car_price * (1 + rate) ** n_value

    if car_income > investment_income:
        break

    n_value += 1

print(f"Minimum service life of the machine: {n_value} years")
