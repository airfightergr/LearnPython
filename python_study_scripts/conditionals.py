# Conditionals...if with logical operators and ternary operator!
# Only difference is not equal. Python: !=, Lua ~= and instead of "then" use ":"

age = 26
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

print("\n")

# use keyword pass if you need an empty block
if age >= 50:
    pass
else:
    print("Pass test\n")

# ----------------------------------------------------------------------------------------
# Logical operators: and, or, not
name = ""
if not name:        # the name is an empty string which equals to False, so name is false here.
    print("Empty string")

name = " "
if name:        # a space is not an empty string!
    print("Not empty string\n")

# Between values...python rocks!
if 18 <= age < 65:
    print("Nice one Python!\n")


# ----------------------------------------------------------------------------------------
# Ternary operator
age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
