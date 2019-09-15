# functions with arbitrary number of args
# This goes give 1 * in the args


def multiply(a, b):
    return a * b


print(multiply(2, 3))


# Put the args into a tuple
def multiply(*mylist):
    print(mylist)


(multiply(2, 3, 4, 5))


# multiply an arbitrary amount of numbers
def multiply(*mylist):
    total = 1
    for number in mylist:
        total *= number
    return total  # if the indentation is the same as above line, returns only the first number!


print(multiply(2, 3, 4, 5))

print("\n------------------\n")
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# The ** !


def save_user(**user):
    print(user)


save_user(id=1, name="admin")


def save_user(**user):
    print(user["name"])


save_user(id=1, name="admin")

