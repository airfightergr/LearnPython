# STRINGS!!!
course = "Python Programming"
print(len(course))  # length of the string
print(course[2])  # then 3nd letter. Python starts at 0 not 1 as in Lua
print(course[-1])  # the last letter! Nice Python!
print(course[2:10])  # a range
print(course[:6])  # get from start to the 7th letter, works [3:] as 4th to end

message = "Python \n\"Programming\""  # "\" is an escape char, if we want to add special chars like quotes. \n works too
print(message)

# Multi line string. If the first word is on the next line, the first line will be empty
multiline = """Python
in
Multiline
"""
print(multiline)

# Concat is the "+" sign instead of ".." in lua
name = "Ilias"
last = "Tselios"
print(name + " " + last)
