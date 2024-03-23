# +-----------+
# | For Loops |
# +-----------+

# iterates through a collection such as values in an array,
#  characters in a string, items in a list etc.
# performs an action each iteration through the collection
# format: for 'item' in 'collection':

# print letters in a string
for letter in "David Limon":
    print(letter)

# print array elements
friends = ["Josh", "Calvin", "Blair"]
for friend in friends:
    print(friend)

# print integers within a range
for digit in range(3, 10):
    # range(x,y) -> array consisting of integers ranging from x to y-1
    # can just be structured as range(x) -> integers from 0 to x-1
    # - i.e. range(x) and range(0, x-1) are identical
    # - i.e. range(x) produces x values, beginning at zero & counting up
    #   to x-1
    print(digit)  # will print integers 3 thru 9 (NOT 3-10)


# print array elements by referring to the numerical pos'n in the array
# creates an array consisting on integers from 0 to the
#  last position in the array
for position in range(len(friends)):
    print(friends[position])
    # same as loop above, but prints by referring the numerical pos'n

# special case command for first iteration
for digit in range(10):
    if digit == 0:
        print("1st iteration")
    else:
        print("Iterating...")
        print(digit)


# +--------------+
# | Exponent Fxn |
# +--------------+

# create fxn to handle exponents
# this does natively exist though; x**y = x^y
def exp(base, exponent):
    result = 1
    if exponent == 0:
        return 1
    elif -1 < exponent < 1:
        # raise ValueError if exponent is actually a root
        raise ValueError(
            "Use an i-th root for exponents between -1 to 1")
    elif base == 0:
        return 0
    else:
        # valid base & exponent; calculate the x^y
        for i in range(abs(exponent)):  # abs account for neg exponent
            result *= base  # result = result * base
        if exponent < 0:
            result = 1 / result
    return result


# +-------------------------+
# | 2D Lists & Nested Loops |
# +-------------------------+

# can create a grid-like structure by defining a list where each element
# is its own list
num_grid = [
    [1, 2, 3],  # "row" 0
    [4, 5, 6],  # "row" 1
    [7, 8, 9],  # "row" 2
    [0]
]

# to print a value, specify which sublist (the "row"), and which pos'n
#  the sublist (the "column")
print(num_grid[1][2])  # prints 6

# can use nested for loops to iterate thru a 2D array
for row in num_grid:
    for col in row:
        print(col)
        # print each number in num_grid in sequential order


# +----------------+
# | Translator Fxn |
# +----------------+

# fxn will replace all vowels in a word/phrase with the letter x
# this method will check each letter and iteratively rebuild the phrase
#  by leaving consonants as-is and using x in place of vowels

def translate(phrase):
    translation = ""
    letter: object
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
            # if the letter being checked is aeiou, it is
            #  a vowel & should be replaced
        else:
            translation = translation + str(letter)
            # if letter being checked is not aeiou, just
            #  leave it as is in the rebuilt translation
    return translation


print(translate(input("Enter a word or phrase: ")))

# +------------+
# | Try/Except |
# +------------+

# used to work around opportunities for invalid code to cause an error
# 'try' block will attempt to run a block of code
# if it runs, the program keeps running
# if an error occurs, the 'except' block will run instead
# except blocks can be specified by type of error

# this block will print 10 / an input integer, but
# text input would cause an error
# if user input 0, 10/0 would throw divide by 0 error
num = int(input("Enter a number: "))
print(10 / num)

# can use except to flag user of incorrect input type
# can use except to alert user of division error
try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError as err_val:  # stores ValueError as a variable
    print("Invalid input type")
except ZeroDivisionError as err_zero:
    print(err_zero)
    # will print "division by zero", the
    #  default exception for ZeroDivisionError


# +------------------+
# | Reading-in Files |
# +------------------+

employee_file = open(
    "C:/Users/dclim/OneDrive/Documents/Code/employees.txt", "r")
# can open .txt, .csv, .html, et al.
# modes:
#   "r" -> read - allows use of data
#   "w" -> write - overwrites data in file
#   "r+" -> read/write
#   "a" -> append - can add to but not replace existing data

print(employee_file.readable())  # returns T/F if can be read
print(employee_file.read())
print(employee_file.readline())
# will print 1st line of data
# running again will print 2nd line of data, and so on

print(employee_file.readlines())
# .readlines will put all lines of data into a list

for employee in employee_file.readlines():
    print(employee)
    # will print each line of data

employee_file.close()  # should always close file at end of use


# can use append mode to add a new employee
employee_file = open(
    "C:/Users/dclim/OneDrive/Documents/Code/employees.txt", "a")

employee_file.write("\nToby - Human Resources")  # must use \n
employee_file.close()

# using write mode will overwrite everything in the file
# using write mode if destination file doesn't exist creates new file
employee_file = open(
    "C:/Users/dclim/OneDrive/Documents/Code/employees.txt", "w")
employee_file.close()


# +---------+
# | Modules |
# +---------+

# import my_module  # runs another .py file, usually with tools
# print(my_module.attribute_fxn())  # runs attribute from my_module.py
