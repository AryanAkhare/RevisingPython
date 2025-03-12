users=['Dave','John','Sara']
data=['dave',42,True]
print('dave' in users)

print(users[0])
print(users[1])
print(users.index('Sara'))
print(users[0:])
print(users[-3:-1])
#add elements

print(len(data))
users.append('Elsa')
print(users)
#add two lists

# users+=data
# print(users)

# data2=['lalaq','']
# data.extend(data2)
# print(data)

#add elements at index
users.insert(0,'Bob')
print(users)

#replacing values
users[1:3]=['Robert', 'jpg']
print(users)

#remove method
users.remove('Bob')
print(users)