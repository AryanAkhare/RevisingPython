str="aryanakhare"

print(str[0:4])
print(len(str))
print(str[-5:-1])
print(str.endswith("e"))
print(str.startswith("a"))
print(str.replace("a","r"))
print(str.capitalize())
print(str.find("ak")) #returns index of first occurence
print(str.count("ar")) #returns total occurence
str="$$$$$$$$$$$$$"
print(str.count("$"))

#multiple lines
multiline='''
Hey , hi are you?

I was just checking in.
 All goOd?
'''
print(multiline)

#escaping special character
sentence='I am Aryan\'s \t gf '
print(sentence)

#string methods
s="Aryanakhare"
print(s.upper())
print(s.lower())
print(len(multiline))
print(multiline.title()) #propercase first letter capital , rest small
print(multiline.count(" "))
multiline+= "Yes good"
print(multiline)
print(len(multiline.strip()))

#Building a menu
title= "menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,".") + "Rs.5".rjust(4))
print("Coffee".ljust(16,".") + "Rs.5".rjust(4))
print("Coffee".ljust(16,".") + "Rs.5".rjust(4))
print("Coffee".ljust(16,".") + "Rs.5".rjust(4))
print("Coffee".ljust(16,".") + "Rs.5".rjust(4))

#string index values
print(s[1])
print(s[1:])
print(s[1:-1])

#retuns boolean
print("aryan".startswith("A"))
print("aryan".endswith("n"))


