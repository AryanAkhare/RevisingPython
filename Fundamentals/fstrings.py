'''#older way
person="Dave"
coins=3
message="\n%s has %s coins left." % (person,coins)
print(message)

#format method
message="\n{} has {} coins left." .format(person,coins)
print(message)

message="\n{1} has {0} coins left." .format(person,coins)
print(message) #using index

message="\n{p} has {c} coins left." .format(p=person,c=coins)
print(message) #using variable names

player={'per':'DAVEYYY','coin':4}
message="\n{per} has {coin} coins left." .format(**player)
print(message) #using dict
'''

#fstrings method
'''player={'per':['Kush','Paras'],'coin':4}
person="Aryan"
coins=5

msg=f"\n{person} has {coins} coins left."
print(msg)

msg=f"\n{person.lower()} has {2*5} coins left."
print(msg) #we can do thing inside this curly base instead of just assigning

msg=f"\n{player['per'][1]} has {2*5} coins left."
print(msg) #using dictionary keys'''

num=10
print(f"\n2.25 times {num} is {2.25*num:.2f}\n")
for x in range(1,11):
    print(f"2.25 times {x} is {2.25342*x:.2f}\n")