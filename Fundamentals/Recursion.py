def add_one(num):
    if(num >= 9):
        return num + 1     # Base case: stop recursion
    total = num + 1
    print(total)           # Print intermediate values
    return add_one(total)  # Recursive call

mynewtotal = add_one(0)
print(mynewtotal)
