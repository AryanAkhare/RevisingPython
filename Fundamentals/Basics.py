# -------------------------------
# Printing and Looping
# -------------------------------

print("Hello world!")

for i in range(3, 10):
    print(f"The square of {i} is {i**2}")

# -------------------------------
# String Comparison and Boolean Type
# -------------------------------

print("dave" == "gray")                # False
print(type("dave" > "gray"))          # <class 'bool'>

# -------------------------------
# Boolean Logic
# -------------------------------

x = True
y = False

print(not x)                          # False
print(x and y)                        # False
print(x or y)                         # True

# -------------------------------
# If-Else Statement
# -------------------------------

meaning = 42

if meaning > 10:
    print("Yes")
else:
    print("No")

# -------------------------------
# Data Types and Type Checking
# -------------------------------

first = "Dave"
last = "Gray"

print(type(first))                    # <class 'str'>

# -------------------------------
# Constructor Function and Type Checking
# -------------------------------

pizza = str("Pep")

print(type(pizza))                    # <class 'str'>
print(type(pizza) == str)             # True
print(isinstance(pizza, str))         # True

# -------------------------------
# Type Conversion
# -------------------------------

a = 2
b = int(2.9)                          # 2 (truncated)

print(a + b)                          # 4

# -------------------------------
# User Input (Commented Out)
# -------------------------------

# name = input("Enter your name: ")
# print("Hi " + name)
