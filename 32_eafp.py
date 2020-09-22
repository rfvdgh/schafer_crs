# Duck Typing and Easier to ask forgiveness than permission (EAFP)
# if it walks like a duck, and quacks like a duck, it's a duck
# this means we don't care what type of object we are working with, we
# only care if our object can do what we ask our object to do.
# we only care about the behavior the object


class Duck:
    def quack(self):
        print("Quack, quack")

    def fly(self):
        print("Flap, Flap!")


class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


# def quack_and_fly(thing):
#     # Not Duck-Typed (Non-Pythonic)
#     if isinstance(thing, Duck):
#         thing.quack()
#         thing.fly()
#     else:
#         print("This has to be a Duck!")


def quack_and_fly(thing):
    pass
    # Pythonic
    # thing.quack()
    # thing.fly()
    # print()

    # LBYL(Non-Pythonic)
    # if hasattr(thing, "quack"):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, "fly"):
    #     if callable(thing.fly):
    #         thing.fly()

    # print()

    # EAFP (Pythonic)
    # try:
    #     thing.quack()
    #     thing.fly()
    #     thing.bark()
    # except AttributeError as e:
    #     print(e)

    # print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

# *** example 2 ***
# person = {"name": "Jess", "age": 23, "job": "Programmer"}
# person = {"name": "Jess", "age": 23}

# # LBYL (Non-Pythonic)
# if "name" in person and "age" in person and "job" in person:
#     print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
# else:
#     print("Missing some keys")

# # EAFP (Pythonic)
# try:
#     print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
# except KeyError as e:
#     print("Missing {} key".format(e))

# *** example 3 ***
my_list = [1, 2, 3, 4, 5, 6]

# Non-Pythonic
# if len(my_list) >= 6:
#     print(my_list[5])
# else:
#     print("That index does not exist")

# Pythonic
# try:
#     print(my_list[5])
# except IndexError:
#     print("That index does not exist")
