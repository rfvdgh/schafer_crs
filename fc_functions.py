def square(x):
    return x * x


def cube(x):
    return x * x * x


# f = square(5)
# We don't want to execute function. We just want to set variable equal to function
# if use parenteses it will execute the function.
f = square

print(square)
print(f(5))

""" we can pass functions as arguments, return functions as the result of other functions
and we can assign functions to variables.
if a function accepts other functions as arguments or returns functions as the result, 
it's considered a higher order function."""


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


# note the lack of parenthese again.
squares = my_map(cube, [1, 2, 3, 4, 5])

print(squares)


def logger(msg):
    def log_message():
        print("Log:", msg)

    return log_message


log_hi = logger("Hi!")
print(log_hi)
# it remembered initial message passed in
log_hi()


def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text


print_h1 = html_tag("h1")
print(print_h1)
print_h1("Test Headline!")
print_h1("Another Headline!")
print_p = html_tag("p")
print_p("Test Paragraph!")

