# Simple function
def hello_world():
    print("Hello World!")

hello_world()

# Function with parameter check (fixed type check)
def sum(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        return 0
    return num1 + num2

total = sum(1, 2)
print(total)

# *args allows multiple positional arguments (returns a tuple)
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", 2.0)

# **kwargs allows multiple keyword arguments (returns a dictionary)
def mul_name_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mul_name_items(a="Dave", b="John", c=2.0)
