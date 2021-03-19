# List in Python uses : square brackets

my_list = ["Tokyo", "London", "New York"]

print my_list             # ['Tokyo', 'London', 'New York']
print my_list[1]          # London

# Updating element value
my_list[2] = "New Delhi"
print my_list             # ['Tokyo', 'London', 'New Delhi']

# Printing all values through for loop
for val in my_list:
    print val

# Output :
# Tokyo
# London
# New Delhi

# Printing length of list
print len(my_list)         # 3

# Inserting in the list :

# Appending at the end
my_list.append("Boston")
print my_list              # ['Tokyo', 'London', 'New Delhi', 'Boston']

# Inserting at some index position
my_list.insert(2, "Durham")
print  my_list             # ['Tokyo', 'London', 'Durham', 'New Delhi', 'Boston']

# Remove operation :
my_list.remove("Tokyo")
print my_list              # ['London', 'Durham', 'New Delhi', 'Boston']

# Pop operation :

# Without providing index it will remove last element of the list
my_list.pop()
print my_list              # ['London', 'Durham', 'New Delhi']

# Pop by providing index position
my_list.pop(1)
print my_list              # ['London', 'New Delhi']

# Delete operation for index position
del my_list[1]
print my_list              # ['London']

# To Delete entire list
del my_list

# Clear also performs the same task as delete but it is added in python 3

fruits = ["apples", "oranges", "cherry"]
print fruits                                        # ['apples', 'oranges', 'cherry']

# Reversing the list
fruits.reverse()
print fruits                                        # ['cherry', 'oranges', 'apples']

# Creating list with multiple data type elements
my_list2 = ["apple", 1, 2, 3.0]
print my_list2                                      # ['apple', 1, 2, 3.0]

# Nested list
my_list3 = ["apple", [1, 2, 3], ['a', 'b', 'c']]
print my_list3                                      # ['apple', [1, 2, 3], ['a', 'b', 'c']]

# Accessing elements in nested list. e.g. accessing 2 from my_list3
print my_list3[1][1]                                # 2