# Getters, Setters, and Deleters
# The purpose of @property is to not break the code for other people using the
# Employee class. The below code intention was to change the email if the first or last
# name were changed. Separating the email from the init into its own method breaks the code
# for others as they will have to access the email with emp_1.email(). The @property allows
# them to access it like an attribute with emp_1.email just like it was in the init method.


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # property defines a method that can be accessed this like an attribute
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):  # name is what you are trying to set
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")
# emp_1.first = "Jim"
emp_1.fullname = "Joe Lee"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
