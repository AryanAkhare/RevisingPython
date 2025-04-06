# ------------------------- Closure Example 1 -------------------------
# A closure is a function having access to the scope of its parent
# even after the parent function has returned.

def parent_function(person, coins):
    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f"\n{person} has {coins} coins left.")
        elif coins == 1:
            print(f"\n{person} has {coins} coin left.")
        else:
            print(f"\n{person} is out of coins.")
    return play_game

# Each call gets its own closure
tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy()
tommy()
jenny()

# ------------------------- Closure Example 2 -------------------------
def outer_function(x):
    def inner_function(y):
        return x - y  # Inner function remembers `x`
    return inner_function

closure_instance = outer_function(10)  # x = 10
print("\nResult of closure_instance(5):", closure_instance(5))  # Output: 5 (10 - 5)
