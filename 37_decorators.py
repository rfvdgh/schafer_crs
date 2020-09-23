# Decorators - functions that takes another function as an argument, adds some type of
# functionality and returns another function. All of this without altering the source code
# of the original function that you passed in.
from functools import wraps  # used when chaining decorators


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(
            "call method executed this before {}".format(
                self.original_function.__name__
            )
        )
        return self.original_function(*args, **kwargs)


# common use case for decorators are for logging. Keep track for how often specific function is run
# and what arguments were passed to that function


def my_logger(orig_func):
    import logging

    logging.basicConfig(
        filename="{}.log".format(orig_func.__name__), level=logging.INFO
    )

    @wraps(orig_func)  # used if chaining decorators
    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)  # used if chaining decorators
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in : {} sec".format(orig_func.__name__, t2))
        return result

    return wrapper


@decorator_function  # equivalent code: display = decorator_function(display)
# @decorator_class
def display():
    print("display function ran")


import time

# @decorator_function  # equivalent code: display_info = decorator_function(display_info)
# @decorator_class
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print("display_info ran with arguments ({}, {})".format(name, age))


# if chaining my_logger and my_timer the result will be:
# display_info = my_logger(my_timer(display_info))

display_info("Tom", 25)

# display()

# decorated_display = decorator_function(display)
# print(decorated_display)
# decorated_display()
