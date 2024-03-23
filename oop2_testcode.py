# +-----------+
# | Test Code |
# +-----------+

from oop2 import Employee
from oop2 import Developer
from oop2 import Manager

emp_1 = Employee('Test', 'User', 60000)
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
mgr_1 = Manager('Sue', 'Smith', 90000, [emp_1, dev_1])

# Variations of printing an instance:
emp_1  # prints __repr__ output
print(emp_1)  # prints  __str__ output
str(emp_1)  # returns __str__ string
print(str(emp_1))  # prints __str__ output
repr(emp_1)  # returns __repr__ string
print(repr(emp_1))  # prints __repr__ output

# getattr(x, "y", "z") returns attribute of object x called y, where y
# is a string (i.e. will return x.y). If "y" is not a defined attribute
# of x (i.e. x.y does not exist), will return default string "z". If no
# default str 'z' is included as an argument and 'y' is not an attribute
# of x, getattr(x, 'y') will return Attribute Error.

# returns 'Shafer', since dev_1.last_name exists
getattr(dev_1, "last_name", "XXX")

# returns "XXX", since dev_1.middle_name does not exist
getattr(dev_1, "middle_name", "XXX")
