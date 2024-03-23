# +-----------+
# | Functions |
# +-----------+


def hello_world():
    print("Hello World!")
# all code in the function must by indented beyond the level where
# the fxn in defined fxns named all lowercase with underscores


hello_world()  # calls the fxn


def say_hi(name):
    # requires name parameter to be given when called
    print("Hello " + name)


say_hi("David")


def cube(base):
    return pow(base, 3)
#       calculates base^3 and returns that value to where cube() was
#       called return breaks out of fxn, so NO CODE CAN COME AFTER
#       return IN A FXN


print(cube(3))  # print 3^3 = 27

# +--------------+
# | If Statement |
# +--------------+

is_male: bool = True
is_tall: bool = True

if is_male:  # condition must be Boolean
    # this code runs <=> is_male is True
    print("You are male.")
else:
    print("You are female")

if is_male and is_tall:  # can use "and" or "or" in condition checks
    print("You're a tall guy.")
elif is_male and not is_tall:  # negatation of parameter is_tall
    print("You're a short guy.")
elif not is_male and is_tall:
    print("You're a tall gal.")
else:
    print("You're a short gal.")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(5, 11, 2))

# comparison operators
#   ==
#   >
#   <
#   >=
#   <=
#   !=


# +--------------+
# | Dictionaries |
# +--------------+

# dictionaries store "keyword:definition" pairs called key:value pairs

# fxn will convert weekday abbreviations to full names
weekdayAbbrev = {
    # this format is called a dict literal (vs. dict constructors)

    # abbrev: fullname
    "M": "Monday",
    "T": "Tuesday",
    "W": "Wednesday",
    "Th": "Thursday",
    "F": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday"
    # all keys must be unique
}

# dict literal getter
print(weekdayAbbrev["W"])      # prints "Wednesday"
print(weekdayAbbrev.get("W"))  # prints "Wednesday"
print(weekdayAbbrev.get("Sept"))  # return then print None
print(weekdayAbbrev.get("Sept", 2**3))  # return & print 8
print(type(weekdayAbbrev.get('Sept', 2**3)))  # returns type = 'int'
print(weekdayAbbrev.get("Sept", "That's not a weekday"))
# key exists -> returns value (the 1st argument)
# key does not exist -> returns 2nd argument
# key does not exist -> no 2nd argument given -> returns None

wk_keys = weekdayAbbrev.keys()
print(wk_keys)
# returns view object of list of keys -- dict.keys(["M", "T", "W", ...])
# view object will show updated dictionary w/o need to rerun wk_keys
wk_vals = weekdayAbbrev.values()
print(wk_vals)  # same as keys() except list of dict.values()
wk_items = weekdayAbbrev.items()
print(wk_items) # same; list of dict.items() (key, value) tuples


# 3 different classes of dict() constructors
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
# kwarg = 'keyword argument', an argument of form 'keyword=value', more
# formally defined as kwarg=value, e.g. def fxn(x=2, y=1) has 2 kwargs
# **kwarg argument allows method call to specify arbitrarily many kwargs

# dict(**kwarg) constructor
algebraic_var_val_kwarg = dict(x=4, y=2, z=1)  # 3 kwargs
# cannot use dict() to create empty dict b/c dict() = None
# can create empty dict like an empty list via dict literal,
# e.g. empty_dict = {}
#
# any operations run on dict() output the operation text,
# e.g. output = dict()  print(output)='output = dict()'

# dict(iterable, **kwarg) constructor
# iterable argument = arbitrarily many arguments in the form of a list
# of (key, value) tuples
algebraic_var_val_iter1 = dict([('x', 4), ('y', 2), ('z', 1)])
# could also remove ('z', 1) tuple from the list, and instead
# pass in z=1 kwarg after the list is close

# zip() takes in 2 arguments: list of keys & list of values, and outputs
# the corresponding iterable (i.e. list of tuples)
algebraic_var_val_iter2 = dict(zip(['x', 'y', 'z'], [4, 2, 1]))
# zip outputs the corresponding iterable, which would then look
# identical to algebraic_var_val_iter1 b/c:
# zip(['x', 'y', 'z'], [4, 2, 1]) = [('x', 4), ('y', 2), ('z', 1)]

# dict(mapping, **kwarg) constructor
# mapping argument is basically an argument in form of dict literal
algebraic_var_val_map1 = dict({'x': 4, 'y': 2, 'z': 1})
# this particular use of dict(mapping) is pretty pointless, since just
# omitting dict() method would have formed a dict literal instead

# like with iterables, any number of the last-most key-value pair
# arguments could instead be passed as kwargs
algebraic_var_val_map2 = dict({'x': 4, 'y': 2}, z=1)


# +-------------+
# | While Loops |
# +-------------+

# will run thru loop until loop guard is false, then
# continue with code block

# Countdown to Launch
def countdown(seconds):
    t = seconds
    print(str(t))
    while t > 0:
        t = t - 1
        print(t)
    print("Ignition.")


countdown(10)

# +---------------+
# | Guessing Game |
# +---------------+

# user will try to guess a secret word
# limit on how many times player can guess before losing

secret_word = "doctor"
guess = ""  # empty string to start
guess_count = 0
guess_limit = 5
game_over: bool = False

# while they have yet to guess the word but still have guesses remaining
while guess != secret_word and not game_over:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess = guess.lower()
        guess_count += 1
    else:
        game_over = True

if game_over:
    print("Out of guesses, you lose.")
else:
    print("You win!")
