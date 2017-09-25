# Arithmetic Operations

print("5 + 2 = ", 5 + 2)
print("5 - 2 = ", 5 - 2)
print("5 / 2 = ", 5 / 2)
print("5 // 2 = ", 5 // 2)
print("5 ** 2 = ", 5 ** 2)
print("5 * 2 = ", 5 * 2)
print("5 % 2 = ", 5 % 2)

# Strings : "this is a string"

print("3 + 22222")

print('\n')  # this just makes new line

asfhj = "asdjhfkasd"
print(asfhj)

suvo_2 = "senpai"
print(suvo_2)

# x = 12 "number"
# print(x)

print("1 + 2 - 3 * 2 = ", 1 + 2 - 3 * 2)

print("(1 + 2 - 3) * 2 = ", (1 + 2 - 3) * 2)

# B-brackets Of D-division M-ultipication A-addition S-substract

string_1 = "My name is     "
string_2 = "Jeff "

string_3 = string_1 + string_2
print(string_3)

# we can reuse variables
print(string_2 * 3)
print('\n')
# -------------------
# Lists

groceries = ["apples", "broccoli", "guava", "cornflakes"]

print("first item is", groceries[0])

groceries.append("pizza")

print(groceries)

groceries.remove("pizza")

print(groceries)

groceries.sort()

print(groceries)

print(len(groceries))

groceries.insert(1, "vodka")
groceries.sort()
print(groceries)

# ----------------------

# Tuple

tuple_1 = (1, 2, 3, 4, 5, 6)

print(tuple_1)

s = ["dominos", "pizza hut"]
print("s", s)
s = ["papajones"]
print("new s", s)
print('\n')
# ----------------- Dictionary -------------------

dict_1 = {"batman": "bruce wayne", "captain cold": "lenoard snart", "pied piper": "thomas peterson"}
dict_2 = {1: "bruce wayne", 2: "lenoard snart", 3: "thomas peterson"}
dict_3 = {"batman": 2345, "captain cold": 3425, "pied piper": 2435}
dict_4 = {"batman": 2335, "captain cold": "lenoard snart", "pied piper": "thomas peterson"}

secret_identity = "shuvo"

dict_5 = {"batman": secret_identity, "captain cold": "lenoard snart", "pied piper": "thomas peterson"}

print(dict_5["batman"])

print(dict_1)
print(dict_2)
print(dict_3)
print(dict_4)

print('\n')
# ---- Conditional Statements ------------------

age = 30
if age > 16:
    print("you're old enough to drive")
else:
    print("you're not old to drive")

# --------

if age >= 21:
    print("you're old enough to drive a tractor")
elif age >= 16:  # elif means Else-If, you can chain conditions together
    print("you're old enough to drive a car")
else:
    print("you're not old enough to drive")

# For Loop

for x in range(0, 10):
    print(x, " ", end="")

# ----------
glist = ["juice", "papya", "potato"]
for x in glist:
    print(x)

# ----------
for i in [2, 3, 4, 5, 6]:
    print(i)

# ----------
number_table = [[1, 2, 3], [33, 44, 42], [123, 234, 345]]

for x in range(0, 3):
    # print(x)
    for y in range(0, 3):
        print(number_table[x][y])
print('\n')
# -------- while loop -------------
i = 0
while (i <= 20):
    if (i % 2 == 0):
        print(i)
    elif (i == 3):
        break
    else:
        i = i + 1
        continue  # skips next iteration of the loop
    i += 1  # shorthand for i = i + 1
