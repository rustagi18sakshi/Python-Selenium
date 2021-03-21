# Tuple in Python uses : ()
# Ordered, indexed, unchangeable and can have duplicates
# Tuples are immutable. So we cannot perform insert, update and delete operation.

my_tuple = ("Apple", "Oranges", "Grapes")

print my_tuple           # ('Apple', 'Oranges', 'Grapes')
print my_tuple[1]        # Oranges
print my_tuple[-1]       # Grapes    -1 means value of last index
print my_tuple[0:2]      # ('Apple', 'Oranges')

# Get length of tuple
print len(my_tuple)      # 3

# To check if element is present in tuple
print "Apple" in my_tuple       # True
print "Cherry" in my_tuple      # False

# FOR loop
for val in my_tuple:
    print val

# Output :
# Apple
# Oranges
# Grapes

# If we perform invalid operation of adding/updating item in tuple :
# my_tuple[2] = "Guava"       # Error received : TypeError: 'tuple' object does not support item assignment

# If we perform invalid operation of deleting item in tuple :
# del my_tuple[1]             # Error received : TypeError: 'tuple' object doesn't support item deletion

# To delete entire tuple
del my_tuple

# Nested tuple : Below one has item, one more tuple, one list
my_tuple2 = ("Banana", (1, 2, 3), ["Tokyo", "New Delhi"])
print my_tuple2                               # ('Banana', (1, 2, 3), ['Tokyo', 'New Delhi'])

# To print particular element in nested tuple
print my_tuple2[2][1]                         # New Delhi

# You can change the mutable items inside the tuple. e.g. below we can change the list item
my_tuple2[2][1]  = "New York"
print my_tuple2                               # ('Banana', (1, 2, 3), ['Tokyo', 'New York'])


