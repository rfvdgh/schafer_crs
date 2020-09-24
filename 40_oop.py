# Object-Oriented Programming


class Employee:

    # class variables
    num_of_emps = 0
    raise_amount = 1.04

    # each method in a class automatically takes the instance as the first argument
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        # when trying to access an attribute on an instance it will first check if instance
        # has that attribute and if it doesn't it'll see if that class or any class it inherits
        # from contains that attribute.
        self.pay = int(self.pay * self.raise_amount)
        # or int(self.pay * Employee.raise_amount)


emp_1 = Employee("joe", "lee", 40000)
emp_2 = Employee("bob", "evans", 50000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# # what's really going on in the background is Employee.fullname(emp_1)
# print(Employee.fullname(emp_1))


# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.__dict__)
# print(Employee.__dict__)

# Employee.raise_amount = 1.05  # changes for the class
emp_1.raise_amount = 1.05  # Instance method...this creates raise_amount attribute within employee 1 namespace
# print(emp_1.__dict__)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print(Employee.num_of_emps)
