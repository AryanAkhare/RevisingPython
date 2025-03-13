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

users.pop()
print(users)

del users[0]
print(users)

#del data
data.clear()
print(data)

#sort
users[1:1]=['dace']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums=[4,231,334,13,5]
nums.reverse()
print(nums)


nums.sort(reverse=True)
print(nums)#Desc
nums.sort()
print(nums)#Asc
#org is modified

#org isnt modified
print(sorted(nums,reverse=True))
print(nums)

#get copying 3 methods
numscopy=nums.copy()
mynums=list(nums)
mycopy=nums[:]
print(nums)
print(numscopy)
print(mynums)
print(mycopy)

############################################

# TUPLES (cant change)
mytuple=tuple(('Dave',42,True))
tuple2=(1,3,2,5,1,4,2,1)
print(tuple2)
#to make chnges in tuple we convert into list and operate
newlist=list(mytuple)
newlist.append('Neil')
newtuple=tuple(newlist)
print(newtuple)
#unpacking 
(one,two,*hey)=tuple2
print(one)
print(hey)

#count occurences 
print(tuple2.count(1))

#index of first occurence
print(tuple2.index(1))