# closure is function having access to scope of its parent 
# after the parent fucntion has returned
#ex1
def parent_function(person,coins):
    #coins=3

    def play_game():
        nonlocal coins
        coins-=1
        
        if coins >1:
            print("\n"+person+" has "+ str(coins)+" coins left.")
        elif coins ==1:
            print("\n"+person+" has "+ str(coins)+" coin left.")
        else:
            print("\n"+person+" is out of coins.")
    return play_game

tommy=parent_function("tommy",3)
jenny=parent_function("jenny",5)
tommy()
tommy()
jenny()

#ex2
def outer_function(x):
    def inner_function(y):
        return x - y  # Inner function remembers `x`
    return inner_function  # Returning the inner function

closure_instance = outer_function(10)  # `x = 10`
print(closure_instance(5))  # Output: 15 (10 + 5)

