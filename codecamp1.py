# +------------------+
# | Print a Triangle |
# +------------------+

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# +-----------+
# | Variables |
# +-----------+

my_name = "David"
david_is_male = True
my_bff = "Josh"
print("I am " + my_name + ", and my best friend is " + my_bff + ".")

# +---------+
# | Strings |
# +---------+

# a string is a block of characters in double quotes
print("David's house.")
print("David's\nhouse.")  # \n inserts a line break
house = "David's house."
house.lower()  # returns copy of string in all lowercase
house.upper()  # returns copy of string in all caps
house.islower()  # True if all characters are lowercase
house.isupper()  # True if all characters are caps
print(house.upper().isupper())  # always True
len(house)  # returns length of house string
house[4]  # returns item at index pos'n 4 within house string = 'd'
print(house.index("v"))  # returns index pos'n of parameter within
#   house string = 2; false if argument is not in string
print(house.replace("David", "Josh"))  # Josh owns the house now

# +------+
# | Math |
# +------+

# can do four fxns by default
10 % 3  # returns 10 mod 3
abs(-5)  # returns absolute value of -5
pow(4, 6)  # returns 4^6
str(2)  # returns 2 as a string
#   must converts numbers to strings to print next to strings
min(4, 6)  # returns smallest value in string
max(4, 6)  # returns largest value in list
round(4.72, 1)  # returns 4.72 rounded to 1 decimal place

david_age = 23
print(david_age)
print(
    "David is " + str(david_age))  # will return concatenation error if
#   david_age is not converted to a string
print(david_age + 1)

from math import *  # open math directory with more math fxns

#   required for all fxn below
print(sqrt(9))  # prints sqrt of 9
floor(3.7)  # rounds parameter DOWN to nearest integer
ceil(3.2)  # rounds parameter UP to nearest integer

# +--------------------+
# | Getting User Input |
# +--------------------+

# input("Please type your age: ")    # displays prompt and allows
# user Input

# subject_age = input("Please type your name: ") # stores user input as
# a variable ALL INPUT STORED AS STRING BY DEFAULT

# age_next_year = subject_age + 1
#   returns concatenation error b/c tried to concatenate string and
#   integer

# subject_age = 35
int(subject_age)  # convert string to an integer
float(subject_age)  # convert string to a floating point number
age_next_year = float(subject_age) + 1

# print("You will be " + age_next_year + " next year")
#   returns concatenation error b/c tried to concatenate number & str
print("You will be " + str(age_next_year) + " next year")

# +--------------+
# | Listy things |
# +--------------+

# list can consist of any combo of strings, numbers, Booleans
name_age_ismale_homestate = ["David"]
age_ismale = [23, True]
name_age_ismale_homestate = name_age_ismale_homestate.extend(age_ismale)
#    adds age_ismale list to name_age_ismale_homestate list
# name_age_ismale_homestate = name_age_ismale_homestate.append("TX")
#   adds homestate to end of list
# name_age_ismale_hometown_homestate = (
#   name_age_ismale_homestate.insert(3, "Houston")
#       inserts Hometown as index 3 in list
# name_age_ismale_homestate = name_age_homestate.remove(True)
#   removes value equal to parameter
# name_age_ismale_homestate.pop()    # removes last value in List
# name_age_ismale_homestate.clear()   # clears list
# name_age_ismale_homestate[1] # returns 23
# name_age_ismale_homestate.index(23)    # returns 1
# name_age_ismale_homestate.count("David")   # returns how many times
#   "David" is in the list
# name_age_ismale_homestate[-2]
#   returns True b/c indexes from end of list

list_lived = ["TX", "CO", "FL", "PA"]
list2 = list_lived.copy()  # defines list2 as a copy of list_lived
#                            as it was at that time
list.sort(list_lived)  # sorts list in ABC or asc numerical order
print(list_lived)
print(list_lived[
      2:])  # returns list of all items in list from index 2 to list end
(list_lived.reverse())  # reverses list order
list_lived = ["TX", "CO", "FL"]
list_lived.append("PA")  # adds "PA" to end of list
# wanted to "append" another  list to the end instead of just 1 value,
# can be done using .extend(appended_list)
list_lived.remove("FL", "PA")  # returned to original state
list_lived.extend(["FL", "PA"])  # (re-)appends  FL & PA list

list_lived.remove("CO")  # deleted CO out of list
list_lived.insert(1, "CO") # re-inserts CO to be back at@ index pos'n 1
print(list_lived)

# list comprehensions
# could create a copy of list_lived one item at a time via for loop
list3 = []
for state in list_lived:
    list3.append(state)

# instead could create do the same via list comprehension, which
# basically says "append(state) to list for each state in list_lived":
list3 = []  # clear list3 before proceeding
list3 = [state for state in list_lived]

# list comprehension if we wanted to define a list to be the list of
# squares of numbers in an original list
base_list = [1, 2, 3, 4, 5]
square_list = [n**2 for n in base_list]

# this is a more readable way to run map()
# basically says "For n in base_list, perform the function of mapping
# each n to n^2
square_list = map(lambda n: n**2, base_list)
# lambda is an anonymous do-nothing fxn, so the return is just a list of
# squares of base_list. IOW, square_list is a copy of base_list where
# all values of n undergo reMAPping to new value of n^2

# kwarg CONSTRUCTOR where each list item evald before being added to new
# list obj via being an argument in  .append() methid
# create a list even numbers in base_list
# for all even numbers, num % 2 = 0; for odds, num % 2 = 1
even_list = []
for n in base_list:
    if n % 2 == 0:
        even_list.append(n)

# concise ITERATIVE list constructor  of same list way to construct
# appending for loop yields n & appends to list <=> n%2 == 0 was
# true (i.e. was even)
even_list = [n for n in base_list if n % 2 == 0]

# lambda function construction of list, going through each n in
# base_list, but selectively yielding (i.e. 'filtering') the evens
even_list = filter(lambda n: n % 2 == 0, base_list)



# pair each letter in abcd into a tuple with number in 1234
pair_list = []
for letter in 'abcd':
    for num in range(4):
        pair_list.append((letter, num))

pair_list = [(letter, num) for letter in 'abcd' for num in range(4)]

# dictionary comprehension
letters = ['a', 'b', 'c', 'd']
nums = [1, 2, 3, 4]
# make a dict of 'letter': num from zipped list (i.e. a dict iterable)
for letter, num in zip(letters, nums):
    zip_dict[letter] = num

# redefine zip_dict, identical end result as before but now created as a
# dict literal
zip_dict = {letter: num for letter, num in zip(letters, nums)}
# run again but exclude (b: 2)
zip_dict = {
    letter: num for letter, num in zip(letters, nums) if letter != 'b'
}



# set comprehensions
# set is a list that has no repeat values
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]

# long way to form set from nums
nums_set = set()  # empty set
for n in nums:
    nums_set.add(n)
print(nums_set)

# concise way to form set from nums, akin to generators
nums_set = {n for n in nums}
print(nums_set)
type(nums_set)


# generator expressions work similarly
nums = [1, 2, 3, 4, 5]
# want to yield n^2 for each number in list
def gen_func(vals):
    for val in vals:
        yield val**2
nums_gen = gen_func(nums)
print(nums_gen)

# quicker way to create identical generator
nums_gen = (n**2 for n in nums)
print(nums_gen)

# prints each string in list (i.e. each state) on separate line
for state in list_lived:
    print(state)

print(len(list_lived))  # =4
print(range(len(list_lived)))  # =range(0,4)

by_twos = (2, 4, 6)  # creates a tuple, which is an immutable list
# could also make a list of tuples, which notably is formed when zipping
# several lists.
