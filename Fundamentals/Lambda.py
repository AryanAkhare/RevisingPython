squaring = lambda num : num*num
print(squaring(5))

addTwo = lambda num: num+2
print(addTwo(2))

multwonum=lambda a,b:a*b
print(multwonum(3,4))

###################
print(f"{'-'*20}")
def function_builder(x):
    return lambda num:num+x

addTen=function_builder(10)
addTwenty= function_builder(20)

print(addTen(7))
print(addTwenty(7))

#################### MAP
print(f"{'-'*20}")
sq=lambda num:num*num
number=[3,7,12,18,20,21]
squared_nums=map(sq,number) 
#map=(function,datacollection)
print(f"This is list of numbers: {list(number)}")
print(f"This is list of squared numbers: {list(squared_nums)}")

#################### Filter
print(f"{'-'*20}")
isOdd=lambda num: num%2 != 0
numbers=[13,242,24,52,3,412,21,321]
Odd_nums=map(isOdd,numbers)
fil_odd=filter(isOdd,numbers)
print(f"list of numbers: {list(numbers)}")
print(f"list is number is odd: {list(Odd_nums)}")
print(f"list filtered with only odd nums:{list(fil_odd)}")
#######################

from functools import reduce #iterable
print(f"{'-'*20}")
print("Sum")
re=lambda acc,curr:acc +curr
numbers=[1,2,3,4,5,1]
total=reduce(re,numbers,10) 
#reduce(func,data,starting_value) here I gave 10 so it gives answer 10+16 as it started from 10
print(total)

print(f"{'-'*20}")
print("Char count in strings")
re2=lambda acc,curr:acc +len(curr)
names=['Davegray','Aryan Akhare','Bohemian Rhapsody','Uptwon']
char_count=reduce(re2,names,0)
 #starting val optional for numbers not strings
print(char_count)
