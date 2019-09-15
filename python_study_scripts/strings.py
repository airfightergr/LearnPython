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
multiline = """
Python
in
Multiline
"""
print(multiline)

# Concat is the "+" sign instead of ".." in lua
name = "Ilias"
last = "Tselios"
full = name + " " + last
print(full)

# Another way to concat... with values, all types
nameNew = "Ilias"
lastNew = "Tselios"
fullnew = f"{name} {last} \n"  # f or F
print(fullnew)

# upper, lower, and title case (the first letter of each word capital
new_course = "   Programming in Python"
print(new_course.upper())
print(new_course.lower())
print(new_course.title())
print(new_course.strip())  # removes white spaces from the start
print(new_course.find("Pyt"))  # returns the index that found the string. -1 if string not found
print(new_course.replace("o", "0"))  # replace part of the string
print("yth" in new_course)  # boolean: if the string exists
print("yth" not in new_course)  # boolean: if the string does not exists

