# ---------- Lambda Functions ----------
squaring = lambda num: num * num
print(squaring(5))

add_two = lambda num: num + 2
print(add_two(2))

multiply_two_numbers = lambda a, b: a * b
print(multiply_two_numbers(3, 4))

# ---------- Lambda with Closure ----------
print(f"{'-'*20}")
def function_builder(x):
    return lambda num: num + x

add_ten = function_builder(10)
add_twenty = function_builder(20)

print(add_ten(7))
print(add_twenty(7))

# ---------- map() Example ----------
print(f"{'-'*20}")
square = lambda num: num * num
numbers_map = [3, 7, 12, 18, 20, 21]
squared_numbers = map(square, numbers_map)
print(f"This is list of numbers: {list(numbers_map)}")
print(f"This is list of squared numbers: {list(squared_numbers)}")

# ---------- filter() Example ----------
print(f"{'-'*20}")
is_odd = lambda num: num % 2 != 0
numbers_filter = [13, 242, 24, 52, 3, 412, 21, 321]
odd_numbers_map = map(is_odd, numbers_filter)
filtered_odd_numbers = filter(is_odd, numbers_filter)
print(f"List of numbers: {list(numbers_filter)}")
print(f"List showing which number is odd (True/False): {list(odd_numbers_map)}")
print(f"List filtered with only odd numbers: {list(filtered_odd_numbers)}")

# ---------- reduce() Examples ----------
from functools import reduce

print(f"{'-'*20}")
print("Sum using reduce:")
sum_reduce = lambda acc, curr: acc + curr
numbers_reduce = [1, 2, 3, 4, 5, 1]
total_sum = reduce(sum_reduce, numbers_reduce, 10)
print(total_sum)

print(f"{'-'*20}")
print("Character count in strings using reduce:")
char_count_reduce = lambda acc, curr: acc + len(curr)
name_list = ['Davegray', 'Aryan Akhare', 'Bohemian Rhapsody', 'Uptwon']
total_chars = reduce(char_count_reduce, name_list, 0)
print(total_chars)
