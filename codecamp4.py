# +-------------------+
# | Classes & Objects |
# +-------------------+

# classes allow you to declare a new data type (like strings, numbers,
# & Booleans, which can be called into other scripts

# creating objects in Student class defined in student.py
from student import Student
from student import GradStudent

student1 = Student("Jim", "Business", 3.1, True)
student2 = Student("Pam", "Art", 3.7, False)
student3 = Student('Josh', 'Engineering', 2.8, False)
print(student1.gpa)  # can access instances' attributes by name
print(student1.enrollment_by_major)  # dict on # of students per major
print(Student.enrollment_by_major)  # same as preceding line

# prints result of a Student instance method with argument student1
print(student1.on_honor_roll())

# defining object in child class GradStudent
# must specify parental __init__ attributes as well as child's
# since parental __init__ method was overridden, but super() was called
grad_student1 = GradStudent("George", "Clinical Psychology",
                            3.8, False, True)
grad_student2 = GradStudent("Jack", "MBA", 3.9, False, False)
grad_student1.graduate()

print(Student.__dict__)


# +--------------------------------+
# | Tuple Class Variable Test Code |
# +--------------------------------+


# this class method works as intended: directly overwrites a
# tuple class variable with new tuple by redefining the tuple within
# the class method
# GradStudent.alter_ui_panel_height()

# Code testing was done inside existing Student & GradStudent classes
# in student.py and then removed. Below, code blocks from student.py
# containing any test code are reproduced at commented out

# class GradStudent(Student):
#     # pass  # if wanted to accept all parental methods/attributes
#
#     # can also define a class that inherits all attributes & methods of
#     # an existing parent class
#     # can also alter & add to parental attributes & methods, or use pass
#     # keyword to accept all parental attributes and method as-is
#     count = 0
#     print(count)  # =0
#     listy = [20, 10]
#     tuple_test = (20, 10)
#     print(tuple_test)  # =(20, 10)
#
#     # overrides parental attributes
#     def __init__(self, name, major, gpa, on_acpro, thesis_done):
#         self.thesis_done = thesis_done
#         super().__init__(name, major, gpa, on_acpro)
#         #   including this allows GradStudent to access parental methods
#         #   incl. attributes from __init__ method
#         type(self).count += 1
#
#     @classmethod
#     def alter_ui_panel_height(cls):
#         tuple_saver = [cls.tuple_test[0], cls.tuple_test[1]]
#         cls.tuple_test = (tuple_saver[0], 10 + 10*cls.count)
#         print('count=' + str(cls.count)
#               + ' so predicted tuple = (20, '
#               + str(10 + 10*cls.count) + ')')
#         print(cls.tuple_test)
