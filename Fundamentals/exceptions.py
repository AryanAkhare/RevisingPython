"""
Exception Handling in Python

This script demonstrates various exception handling concepts, including:
- Basic try-except
- Handling multiple exceptions
- Using else and finally
- Raising exceptions manually
- Defining custom exceptions
"""

# 1. Basic Exception Handling
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Enter a number.")

# 2. Handling Multiple Exceptions
try:
    lst = [1, 2, 3]
    print(lst[5])
except (IndexError, KeyError):
    print("Index or Key Error occurred.")

# 3. Using else and finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result:", result)
finally:
    print("Execution completed.")

# 4. Raising Exceptions
num = -5
if num < 0:
    raise ValueError("Negative numbers are not allowed!")

# 5. Custom Exceptions
class NegativeNumberError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

try:
    check_number(-3)
except NegativeNumberError as e:
    print(e)
