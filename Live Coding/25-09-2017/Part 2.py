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

# -------------- order of operations -------------------
# B-brackets Of D-division M-ultipication A-addition S-substract

print("1 + 2 - 3 * 2 = ", 1 + 2 - 3 * 2)

print("(1 + 2 - 3) * 2 = ", (1 + 2 - 3) * 2)

# ----------- combining strings -----------------------
string_1 = "My name is     "
string_2 = "Jeff "

string_3 = string_1 + string_2
print(string_3)

# we can reuse variables, here i've reused the string_2
print(string_2 * 3)
print('\n')

# ------------------- Lists -----------------------------

groceries = ["apples", "broccoli", "guava", "cornflakes"] # declare the list first

print("first item is", groceries[0]) 

groceries.append("pizza") # add another item

print(groceries) # print the list after adding an item

groceries.remove("pizza") # remove the item

print(groceries) # print after removing the item

groceries.sort() # uses built in sorting algorithm, this is not efficient in a normal usage scenario. Professional cases we write this ourselves

print(groceries)

print(len(groceries)) # this prints how many items are there in the list, hence. len() is length

# all lists start counting from 0 to n'th value
groceries.insert(1, "vodka") # here we are adding item to 1st position, in human terms its the second position

groceries.sort() # if you want to keep the list sorted, you got to sort again. Otherwise if you need a sorted list you gotta build it yourself

print(groceries)

# ---------------------- Tuple ---------------------

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

# you can use variables inside dictionaries
dict_5 = {"batman": secret_identity, "captain cold": "lenoard snart", "pied piper": "thomas peterson"}

print(dict_5["batman"]) # what happens when you print the reference to batman ?

# print(dict_1)
# print(dict_2)
# print(dict_3)
# print(dict_4)

print('\n')

# --------------- Conditional Statements ------------------

# only 1 condition exsists
age = 30
if age > 16:
    print("you're old enough to drive")
else:
    print("you're not old to drive")

# more than 1 condition exists, therefore you can chain conditions by using 'elif ... : '
if age >= 21:
    print("you're old enough to drive a tractor")
elif age >= 16:  # elif means Else-If, you can chain conditions together
    print("you're old enough to drive a car")
else:
    print("you're not old enough to drive")

# ----------- For Loop ---------------

# iterate x from 0 upto, but not including 10
for x in range(0, 10):
    # reason why we did this is, we defined end of the string is a invisible space, 
    #so each time print is used plug the next item to the back of the previous printed item
    print(x, " ", end=" ") 
    
#     print(x)  # try uncommenting this, 
#     print(x, " ") # try uncommenting this, 

# ----------

glist = ["juice", "papya", "potato"]
# print all items in the list one by one
for x in glist:
    print(x)

# ----------
# for i'th item in list, only difference here is we defined the list inside the loop
for i in [2, 3, 4, 5, 6]:
    print(i)

# ----------
# this is 3 lists inside a list
number_table = [[1, 2, 3], [33, 44, 42], [123, 234, 345]]

for x in range(0, 3): # print x'th item upto, but not including 3rd
    # print(x)
    for y in range(0, 3):
        print(number_table[x][y])
print('\n')

# -------- while loop -------------

i = 0
while (i <= 20):
    if (i % 2 == 0):
        print(i)
    elif (i == 3): # you can change this value and see at what point the code will stop executing
        break
    else:
        i = i + 1
        continue  # skips next iteration of the loop, just tells the code to keep continuing
    i += 1  # shorthand for i = i + 1 / if not provided your code will run an infinite loop where it cannot be stopped
