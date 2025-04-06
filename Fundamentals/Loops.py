# -------------------- FOR LOOP --------------------

# Simple range loop
for i in range(0, 5):
    print(i)

# Looping through a list
name = ["dave", "lisa", "john"]
for x in name:
    print(x)

# Looping through a string
for x in "Mississippi":
    print(x)

# Break example
for x in name:
    if x == "lisa":
        break
    print(x)

# Continue example
for x in name:
    if x == "lisa":
        continue
    print(x)  # Skips "lisa"

# Range from 2 to 3
for i in range(2, 4):
    print(i)

# Multiples of 5 from 0 to 100
for i in range(0, 101, 5):
    print(i)

# Nested loop
names2 = ["dave", "Sara", "john"]
actions = ["codes", "eats", "sleeps"]

for x in names2:
    for i in actions:
        print(x + " " + i + ".")

# -------------------- WHILE LOOP --------------------

value = 1
while value < 10:
    print(value)
    value += 1
