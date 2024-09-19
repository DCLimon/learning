# class variables


class Employee:

    # class attributes may be called as either:
    #   - a class attribute: Employee.raise_amt <- cleaner way to do it
    #   - an instance attribute that is common to all instances of the
    #     class: emp1.raise_amt = emp2.raise_amt = Employee.raise_amt
    #
    # BUT BEWARE: redefining self.raise_amt changes that value only for
    # the instance, not for the entire class
    raise_amt = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = (
            f'{first_name.lower()}.{last_name.lower()}@company.com'
        )

    # not a @property method because just want a way to easily obtain
    # the full name, but the attributes exist already as separate first
    # & last names
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

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
        # end user can just call Employee.from_string('first-last-pay')
        # instead of needing to do emp_str.split('-') on each emp_str
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static methods are relevant to the class in which they exist, but
    # use neither self nor cls as arguments -- basically a normal fxn,
    # but only relevant to the class where they are defined
    @staticmethod
    def is_workday(day):
        # day format: datetime.date(yyyy, mm, dd)
        # .weekday() assigns number to each day of the week, where
        # Monday = 0, Saturday = 5, Sunday = 6, etc.
        if day.weekday() >= 5:
            return False
        else:
            return True


# +-----------+
# | Test Code |
# +-----------+

emp_1 = Employee('Test', 'User', 60000)
emp_2 = Employee('Corey', 'Schafer', 50000)

# can call Employee.raise_amt or self.raise_amt

# can redefine raise_amt for a single employee by running
# emp_1.raise_amt = 1.05 (leaving Employee.raise_amt=1.04)

# employee string to test Employee.from_string alternate constructor
emp_str_1 = 'John-Doe-70000'
emp_3 = Employee.from_string(emp_str_1)
