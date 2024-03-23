# +-------------------+
# | Classes & Objects |
# +-------------------+

# classes allow you to declare a new data type (like strings, numbers,
# & Booleans, which can be called into other scripts

# can also declare fxns for objects that are intrinsic to a class, which
# are called "methods"


class Student:
    enrollment_by_major = {}
    # class variable called by Student.variable
    # can be called by cls.variable within class methods
    # dictionary where key=major, value=enrollment

    # __init__(self) creates an instance of the class, & creates
    # attributes that define a class
    def __init__(self, name, major, gpa, on_acpro):
        # self generically refers to any given instance of class

        # self.name = name declares that the name attribute of a given
        # instance should be the name parameter passed in
        self.name = name
        self.major = major
        self.gpa = gpa
        self.on_acpro = on_acpro
        self.enroll()

        pass  # allows __init__ to be passed to child classes

    def __repr__(self):
        return (
            f'Student type: undergraduate\n'
            f'Name: {self.name}\n'
            f'Major: {self.major}, GPA: {self.gpa}\n'
            f'Is on academic probation?: {self.on_acpro}'
        )

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    def enroll(self):
    # Update enrollment_by_major dictionary count, or add student's
    # major to dictionary if not already there.  self.enroll() is run as
    # part of self.__init__()
        if Student.enrollment_by_major.get(self.major):
            # If student's major already listed in major enrollment
            # dict, add +1 to count of students in that major.
            Student.enrollment_by_major.update({
               self.major: Student.enrollment_by_major.get(self.major)+1
            })
        else:
            # If student's major not listed in enrollment dict, add the
            # major to the dict and set enrollment count to 1.
            Student.enrollment_by_major.update({self.major: 1})


class GradStudent(Student):
    # pass  # if wanted to accept all parental methods/attributes

    # can also define a class that inherits all attributes & methods of
    # an existing parent class
    # can also alter & add to parental attributes & methods, or use pass
    # keyword to accept all parental attributes and method as-is

    # overrides parental attributes
    def __init__(self, name, major, gpa, on_acpro, thesis_done):
        self.thesis_done = thesis_done
        super().__init__(name, major, gpa, on_acpro)
        #   including this allows GradStudent to access parental methods
        #   incl. attributes from __init__ method

    def graduate(self):
        if self.thesis_done:
            print(self.name + " is now Dr. " + self.name)
            self.name = "Dr. " + self.name
            # should implement __del__(self) method to remove grads
        else:
            print("Must complete thesis before graduating")
