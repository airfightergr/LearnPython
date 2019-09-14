# Variables - Python is dynamic language like LUA - no need to declare variable type
studentsCount = 1000
rating = 4.99
is_published = False
course = "Python Programming"
value1, value2 = 1, 2

# Variables we still can annotate/hint
x: int = 1
print(x, "int declared")



# LISTS! or arrays or tables in LUA with the use of [] instead of {}
myList = [1, 2, 3, 4, 6]
print(myList[2])  # we call a member of the list the same way as in Lua
print(myList)
