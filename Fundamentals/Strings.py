# ---------------- Basic String Indexing and Properties ---------------- #
str1 = "aryanakhare"

print(str1[0:4])               # 'arya'
print(len(str1))               # 11
print(str1[-5:-1])             # 'khar'
print(str1.endswith("e"))      # True
print(str1.startswith("a"))    # True
print(str1.replace("a", "r"))  # replaces all 'a' with 'r'
print(str1.capitalize())       # 'Aryanakhare'
print(str1.find("ak"))         # index of first occurrence: 5
print(str1.count("ar"))        # 2

# Replace entire string with repeated char and count
str1 = "$$$$$$$$$$$$$"
print(str1.count("$"))         # 13

# ---------------- Multi-line and Escape Characters ---------------- #
multiline = '''
Hey , hi are you?

I was just checking in.
 All goOd?
'''
print(multiline)

sentence = 'I am Aryan\'s \t gf '
print(sentence)  # includes escaped apostrophe and tab

# ---------------- String Methods ---------------- #
s = "Aryanakhare"
print(s.upper())        # ALL CAPS
print(s.lower())        # all lowercase
print(len(multiline))   # length including whitespace/newlines
print(multiline.title())# First letter of each word capital
print(multiline.count(" ")) # count of spaces
multiline += "Yes good"
print(multiline)
print(len(multiline.strip())) # removes leading/trailing whitespaces

# ---------------- Build a Menu with Alignment ---------------- #
title = "menu".upper()
print(title.center(20, "="))
for _ in range(5):
    print("Coffee".ljust(16, ".") + "Rs.5".rjust(4))

# ---------------- String Index and Boolean Checks ---------------- #
print(s[1])          # 'r'
print(s[1:])         # 'ryanakhare'
print(s[1:-1])       # 'ryanakhar'

print("aryan".startswith("A"))  # False (case-sensitive)
print("aryan".endswith("n"))    # True
