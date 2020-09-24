from collections import namedtuple

# list
# color = (55, 155, 255)
# print(color[0])

# dict
# color = {"red": 55, "green": 155, "blue": 255}
# print(color["red"])

# named tuple
Color = namedtuple("Color", ["red", "green", "blue"])
color = Color(
    blue=55, green=155, red=255
)  # don't need the blue, green and red, just the numbers

white = Color(255, 255, 255)

print(color.red)
print(color[0])
print(white.blue)
