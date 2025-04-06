# -------------------- LISTS --------------------
users = ['Dave', 'John', 'Sara']
data = ['dave', 42, True]

print('dave' in users)  # False (case-sensitive)

# Accessing elements
print(users[0])
print(users[1])
print(users.index('Sara'))
print(users[0:])
print(users[-3:-1])

# Add elements
print(len(data))
users.append('Elsa')
print(users)

# Insert at index
users.insert(0, 'Bob')
print(users)

# Replace slice
users[1:3] = ['Robert', 'jpg']
print(users)

# Remove by value
users.remove('Bob')
print(users)

# Pop last item
users.pop()
print(users)

# Delete by index
del users[0]
print(users)

# Clear and print
data.clear()
print(data)

# Sorting
users[1:1] = ['dace']  # Inserting at index 1
users.sort()
print(users)  # Alphabetical
users.sort(key=str.lower)
print(users)  # Case-insensitive

# Numbers
nums = [4, 231, 334, 13, 5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)  # Descending

nums.sort()
print(nums)  # Ascending

# Sorted (doesn't modify original)
print(sorted(nums, reverse=True))
print(nums)

# Copying lists
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(nums)
print(numscopy)
print(mynums)
print(mycopy)

# -------------------- TUPLES --------------------
mytuple = tuple(('Dave', 42, True))
tuple2 = (1, 3, 2, 5, 1, 4, 2, 1)
print(tuple2)

# Convert tuple to list to modify
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

# Unpacking tuple
(one, two, *hey) = tuple2
print(one)
print(hey)

# Count and index
print(tuple2.count(1))
print(tuple2.index(1))
