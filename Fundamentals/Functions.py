def hello_world():
    print("Hello World!")

hello_world()

def sum(num1,num2):
    if type(num1 is not int or type(num2) is not int):
        return 0
    return num1+num2
total=sum(1,2)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave","John",2.0)

def mul_name_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mul_name_items(a="Dave",b="John",c=2.0)