# +------------+
# | Subclasses |
# +------------+

# will create 'Developer' & 'Manager' subclasses of Employee class


class Employee:

    raise_amt = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    # @property method defines a new instance variable (i.e. one not
    # defined by __init__) as the output of a method, allowing code
    # to call the attribute either:
    #   - like an instance method: emp.full_name()
    #   - like an instance variable: emp.full_name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # setter allows redefining a property to change all relevant
    # attributes to match. Called by emp_1.full_name = 'New Name'
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    # deleter runs a cleanup fxn when deleting an instance. Called by
    # del emp_1.full_name
    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None
        self.pay = None

    @property
    def email(self):
        return (f"{self.first_name.lower()}.{self.last_name.lower()}"
                f'@company.com')

    # __repr__ is unambiguous, for other devs
    def __repr__(self):
        return (f"Employee('{self.first_name}', '{self.last_name}', "
                f"'{self.pay}')")

    # __str__ may be ambiguous, for end users in easy-reading format
    def __str__(self):
        return f'{self.full_name} - {self.email}'

    # will define how to add when performing emp_1 + emp_2
    def __add__(self, other):
        return self.pay + other.pay

    # standard instance method, which alters an instance variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, new_raise_amt):
        cls.raise_amt = new_raise_amt

    # can use class methods as "alternate constructors", i.e. a method
    # that creates new instance of a class given different info
    @classmethod
    def from_string(cls, emp_str):
        # creates new employee from a 'first-last-pay' string, so that
        # end user can just call Employee.from_string(emp_string)
        # instead of needing to run emp_string.split('-') on each
        # emp_str.
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static methods are relevant to the class in which they exist, but
    # use neither self nor cls as argument -- basically a normal fxn,
    # but only relevant to the class where they are defined
    # Called by Employee.is_workday(day)
    @staticmethod
    def is_workday(day):
        # day format: datetime.date(yyyy, mm, dd)
        # .weekday() assigns number to each day of the week, where
        # Monday = 0, Saturday = 5, Sunday = 6, etc.
        if day.weekday() >= 5:
            return False
        else:
            return True


# Class(OtherClass1, OtherClass2), OtherClass = classes to inherit from
class Developer(Employee):
    # pass -- this would be the only subclass code if wanted Developer
    # to have identical attributes to Employee

    # devs get 5%/y raise, which can be inherited by subclasses but
    # does not afx general Employee.raise_amt
    raise_amt = 1.05

    def __init__(self, first_name, last_name, pay, prog_lang):
        # overrides Employee.__init__, so must restate all attributes
        # stated b/c wanted to add dev's prog_lang attribute

        # lets Developer.__init__ inherit existing attributes as defined
        # in the superclass by Employee.__init__
        super().__init__(first_name, last_name, pay)
        # could also run this line as
        # Employee.__init__(self, first_name, last_name, pay), but this
        # syntax gets unwieldy for complex inheritance cases

        self.prog_lang = prog_lang


class Manager(Employee):

    raise_amt = 1.10

    # managers will have a list of employees under them
    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)

        # done here for e.g. of if/else; better ways exist to do this:
        #   - set kwarg employees=[] & self.employees = employees
        #   - use @property method for self.employees
        #       - using **kwargs in __init__ parameters?
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # add employee to manager's employee list
    #
    # if self.employees is a @property method, then add_emp needs to be
    # a property setter
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # remove employee from manager's employee list
    #
    # if self.employees is a @property method, then add_emp needs to be
    # a property deleter
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # print manager's employee roster
    def print_emps(self):
        for emp in self.employees:
            print(emp.full_name)

# print(help(Developer))
# shows a 'Method Resolution Order' listing several classes. These are
# the classes where Python will look for existing methods to use (e.g.
# __init__(self), in the order in which it will look.
# Python will use any methods defined in a subclass where possible,
# defaulting to parent class if objects do not exist in subclass.
