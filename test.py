# Variables - Python is dynamic language like LUA - no need to declare variable type
studentsCount = 1000
rating = 4.99
is_published = False
course_name = """ 
multiple
lines
"""
ax, ay = 1, 2

# Variables we still can annotate/hint
x: int = 1
print(x, "int declared")

# STRINGS!!!
course = "Python Programming"
print(len(course))  # length of the string
print(course[2])    # then 3nd letter. Python starts at 0 not 1 as in Lua
print(course[-1])   # the last letter! Nice Python!
print(course[3:9])  # a range
print(course[:6])   # get from start to the 7th letter, works [3:] as 4th to end


# LISTS! or arrays or tables in LUA with the use of [] instead of {}
myList = [1, 2, 3, 4, 6]
print(myList[2])  # we call a member of the list the same way as in Lua
print(myList)
