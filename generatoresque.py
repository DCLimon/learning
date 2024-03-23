# +------------------+
# | Lambda Functions |
# +------------------+

# lambda is an anonymous fxn, i.e. a fxn that must be declared every
# time it is called, because it has no memory.
# Declared on 1 line (like generators), o/w usual fxn declaration format

# lambda fxn that  adds  x + y
(lambda x, y: x + y)(3, 4)  # adds x=3 + y=4

# Usually used to define fxn for 1-off use, e.g. in a print statement.
print(3 + 4)  # prints 7
print((lambda x, y: x + y)(3, 4))  # prints 7

# Defining a variable as a lambda fxn is the same as declaring the fxn
# in the usual manner, but is very un-Pythonic
xy_add_lambda = lambda x, y: x + y  # Equivalent to xy_add_usual()


def xy_add_usual(x, y):  # Civilized way to declare a fxn
    return x + y


print(xy_add_lambda(3, 4))  # prints 7
print(xy_add_usual(3, 4))  # prints 7

# +---------------------+
# | List Comprehensions |
# +---------------------+

# Used to create a list 1 item at a time, using a for loop.
# e.g. Useful if wanted a list of all values in range(0.9), as below:
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# The simpleton way of doing this is via a classic for loop.
my_list = []
for n in num_list:  # for n in range(0, 9) would give same result
    my_list.append(n)
print(my_list)

# A more elegant (but identical) way is via a list comprehension.
# List comprehension defines the list via a for loop, structure much
# like a generator.

# List comprehension w/ identical result  to for loop above.
# "For n in num_list, append n to my_list"
my_list = [n for n in num_list]  # [n for n in range(0,9)] is identical
print(my_list)

# Create list of squares of num_list using for loop.
square_list = []
for n in num_list:
    square_list.append(n ** 2)
print(square_list)

# Create list of squares of num_list using list comprehension.
square_list = [n**2 for n in num_list]
print(square_list)

# An antiquated equivalent to list comprehension is the map/lambda fxn.
# map() fxn takes map(my_func, my_iter) and applies my_func fxn to each
# item in the my_iter.
# A lambda fxn can passed as my_func argument in a map function.
square_list = map(lambda n: n ** 2, num_list)

# map functions apply my_func to next item in my_iter on an as-requested
# basis, like generators.
# Printing map fxn result returns memory location of map object, b/c
# the values of each my_func(my_iter[n]) are only calculated at runtime.
print(square_list)  # returns <map object at 0x0000029529D29160>
print(list(square_list))  # prints list from map function iterations

# Create list of even numbers from num_list.

# Via for loop.
evens_list = []
for n in num_list:
    if n % 2 == 0:
        # x mod(2)=0 if x is even, x mod(2)=1 if x is odd.
        evens_list.append(n)
print(evens_list)

# Via list comprehension.
# "For n in num_list, if n%2 = 0, append that n to evens_list."
evens_list = [n for n in num_list if n % 2 == 0]
print(evens_list)

# Via filter & lambda fxns.
#
# filter() takes same args as map(), and only returns values of iterable
# for which the function evaluates True.
# Like map(), filter() only applies the fxn to next value of the
# iterable (and filters that value) as-requested, like a generator.
evens_list = filter(lambda n: n % 2 == 0, num_list)
print(evens_list)  # returns <filter object at 0x000001503FF126D8>
print(list(evens_list))

# Create a list of (letter, number) tuples for each letter-number combo
# for each letter in "abcd" & each number in "0123"
#
# Via for loop.
tuple_list = []
for letter in "abcd":
    for num in range(4):
        tuple_list.append((letter, num))
print(tuple_list)

# Via list comprehension.
tuple_list = [(letter, num) for letter in "abcd" for num in range(4)]
print(tuple_list)

# +---------------------------+
# | Dictionary Comprehensions |
# +---------------------------+

# Create a {name: hero} dict.
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heroes = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]
hero_dict = {}  # empty dict

# Via for loop:
for name, hero in zip(names, heroes):
    hero_dict[name] = hero
print(hero_dict)

# Via dict comprehension
hero_dict = {name: hero for name, hero in zip(names, heroes)}
print(hero_dict)

# Can exclude 1 (key, val) tuple from dict by including an if condition
arachnophobe_dict = {name: hero for name, hero in zip(names, heroes)
                     if (name != "Peter" and hero != "Spiderman")}
print(arachnophobe_dict)


# +--------------------+
# | Set Comprehensions |
# +--------------------+

# A set is an iterable, like a list but w/o any repeated values, and
# sorted alphabetically/ascending regardless of input order.

# set constructor from a list (duplicate values excluded):
my_list = [0, 0, 1, 1, 6, 2, 2, 5, 3, 3, 4, 4]
my_set = set(my_list)
print(my_set)  # {0, 1, 2, 3, 4, 5, 6}

# set literal (duplicate values excluded):
my_set = {0, 0, 1, 1, 6, 2, 2, 5, 3, 3, 4, 4}  # cannot use {my_list}
print(my_set)  # {0, 1, 2, 3, 4, 5, 6}

# Via for loop:
my_set.clear()
for n in my_list:
    # set().add will skip attempts to add values already in the set
    my_set.add(n)
print(my_set)  # {0, 1, 2, 3, 4, 5, 6}

# set literals cannot accept a list variable, e.g. my_set = {my_list}.
# However, a set comprehension can accomplish the same thing.
my_set.clear()
my_set = {n for n in my_list}
print(my_set)


# +---------------------+
# | Generator Functions |
# +---------------------+

# list comprehension for reference:
num_list = [n for n in range(10)]
square_list = [n**2 for n in num_list]

# Generator *functions* look like a normal function, except end with
# 'yield x' instead of 'return x'. Each iteration of the generator only
# runs as-requested.


def gen_func(nums):
    # generator function to square values in a list
    for num in nums:
        yield num**2


# Generators run when requested, so must be made into a list, o/w will
# just return generator object memory location
square_list.clear()
for i in gen_func(num_list):
    # Successively adds squared value yielded by gen_fun to square_list,
    # & prints it. Each value is only yielded when this loop calls it.
    square_list.append(i)  # counterproductive to make list from gen
    print(i)
print(square_list)

# Generator *expressions* look like a list/dict comprehension, except w/
# () instead of [] or {}. Also only yield a value when requested.
#
# Unlike generator functions, which can pass in arguments, generator
# expressions require the iterator list to be input by name.
square_list.clear()
gen_exp = (num**2 for num in num_list)
for i in gen_exp:
    square_list.append(i)  # counterproductive to make list from gen
    print(i)
print(square_list)
