name="Dave" 
count=1# global scope

# def greet():
#     print(name)
# greet()


##here name is local scope of the function

def another():
    color="blue"
    global count
    count+=1
    print(count)
    def greeting(name):

        print(color)
        print(name)
    greeting("Dave")
another()