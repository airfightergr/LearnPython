# Oh wow! We reach functions!
# def instead of function in lua
# must have 2 empty lines before and after!


def increment(number, by):
    return number + by


print(increment(2, 3))


def increment(number, by):
    return number, number + by


print(increment(2, 3))


def increment(number, by):
    return number + by


print(increment(2, by=3))   # Use a keyword so the code is readable


def addition(number, plus):
    return number + plus


print(addition(2, plus=8))


def increment(number, by=3):    # can set the value here
    return number + by


print(increment(5))


# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ANNOTATION (if needed)


def increment(number: int, by: int = 25) -> int:
    return number + by


print(increment(50))

# return a tuple , ie: (2, 3) etc. Tuple is like list but cannot be edited


def increment(number: int, by: int = 25) -> tuple:
    return number, number + by, by


print(increment(50))





