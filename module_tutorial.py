# sys.path is where python knows where to find module locations
import sys
import random

# from my_module import *
# import my_module as mm
from my_module import find_index, test

# sys.path.append("/home/poopmonkey/python_code")


courses = ["History", "Math", "Physics", "CompSci"]
random_course = random.choice(courses)

index = find_index(courses, "Math")
# print(index)
# print(test)
print(sys.executable)  # location of python interpreter
print(sys.path)
print(random_course)
