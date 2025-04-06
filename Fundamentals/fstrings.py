# ------------------------- String Formatting Methods -------------------------

# Older % formatting
person = "Dave"
coins = 3
message = "\n%s has %s coins left." % (person, coins)
print(message)

# format() method
message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(person, coins)  # Using index
print(message)

message = "\n{p} has {c} coins left.".format(p=person, c=coins)  # Using variable names
print(message)

# format() using a dictionary
player = {'per': 'DAVEYYY', 'coin': 4}
message = "\n{per} has {coin} coins left.".format(**player)
print(message)

# ------------------------- f-Strings (Python 3.6+) -------------------------

player = {'per': ['Kush', 'Paras'], 'coin': 4}
person = "Aryan"
coins = 5

msg = f"\n{person} has {coins} coins left."
print(msg)

msg = f"\n{person.lower()} has {2 * 5} coins left."
print(msg)  # Expression inside {}

msg = f"\n{player['per'][1]} has {2 * 5} coins left."
print(msg)  # Dictionary access

# ------------------------- Formatting Numbers -------------------------

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

# Multiples of 2.25 (up to 2 decimal places)
for x in range(1, 11):
    print(f"2.25 times {x} is {2.25342 * x:.2f}")
