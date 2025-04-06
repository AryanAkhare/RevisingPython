name = "Dave"       # global
count = 1           # global

def another():
    color = "blue"  # local to 'another'
    global count    # accessing and modifying global 'count'
    count += 1      # count becomes 2
    print(count)

    def greeting(name):
        print(color)  # accesses 'color' from outer function scope
        print(name)   # uses parameter

    greeting("Dave")

another()
