# For loop. No need for end. Uncomment to test

# for x in "Python":
#     print(x)
#

# 5 is not a number, but the number of iterations! Range is special type, does not return list!
# for x in range(5):
#     print(x)
# print("--------")

# change the start
# for x in range(2, 5):
#     print(x)
# print("--------")

# with steps
# for x in range(0, 10, 2):
#     print(x)
# print("--------")

# ----------------------------------------------------------------------------------------
# Lists

names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):    # Another nice one Py!
        print("Found")
        break
else:
    print("Not Found")

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# WHILE LOOP

guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
else:
    print("Correct!")





