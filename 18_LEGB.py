"""
LEGB
Local, Enclosing, Global, Built-in
"""
import builtins

# print(dir(builtins))


# def min():
#     pass


# m = min([5, 3, 2, 1, 6])
# print(m)

x = "global x"


def test(z):
    # global x
    x = "local x"
    # print(x)
    print(z)


# test("local z")
# print(x)

# example of enclosing. Same concept as global and local.
def outer():
    x = "outer x"

    def inner():
        # nonlocal x  # similar to global statement
        x = "inner x"
        print(x)

    inner()
    print(x)


outer()
