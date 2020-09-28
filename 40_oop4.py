# Magic/Dunder Methods
# repr and str methods help with how objects are printed and displayed
# without them printing the employee will give a vague message
# magic methods should not be called directly by programmer, they are
# normally called by interpreter itself.


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # meant to be unambiguous representation of the object.
    # used for debugging and logging and things like that
    # meant to be seen by developers
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # meant to be a more readable representation of object
    # meant to be seen by end user
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Joe", "Lee", 50000)
emp_2 = Employee("Test", "Employee", 60000)

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))
# # same as the below
# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(1 + 2)
# print(int.__add__(1, 2))
# print(str.__add__("a", "b"))


print(emp_1 + emp_2)

print(len("test"))
print("test".__len__())

print(len(emp_1))
