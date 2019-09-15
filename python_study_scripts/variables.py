# Variables - Python is dynamic language like LUA - no need to declare variable type
# The same scheme with local/global variables. But you don't use the "local" as in Lua.
# Python knows that is local if is inside a scope (function , if, etc).
# To modify a global inside a scope, you must the "global" in front of the variable. Not a good practice!
studentsCount = 1000
rating = 4.99
is_published = False
course = "Python Programming"
value1, value2 = 1, 2

# Variables we still can annotate/hint
x: int = 1
print(x, "int declared")

# use capital letters to declare that this constant. You can change it of course
# mostly for other devs not mess with this one!
PI = 3.14

# LISTS! or arrays or tables in LUA with the use of [] instead of {}
myList = [1, 2, 3, 4, 6]
print(myList[2])  # we call a member of the list the same way as in Lua
print(myList)
