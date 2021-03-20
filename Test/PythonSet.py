# Set in Python uses : {}
# Unordered, unindexed, No duplicates

my_set = {"Chalk", "Duster", "Board"}
print my_set              # set(['Chalk', 'Board', 'Duster'])

# print my_set[1]         # Not possible since it is unindexed

# Get length of set
print len(my_set)      # 3

# For loop for printing
for val in my_set:
    print val

# Output :
# Chalk
# Board
# Duster

# To check if element is present in tuple
print "Chalk" in my_set       # True
print "grape" in my_set       # False

# Adding element. Element will be added at any index since Set is unordered
my_set.add("Pen")
print my_set               # set(['Chalk', 'Pen', 'Board', 'Duster'])

# For adding multiple elements use : update
my_set.update(["Pencil", "Eraser"])
print my_set               # set(['Pencil', 'Duster', 'Chalk', 'Pen', 'Board', 'Eraser'])

# Remove operation through element value
my_set.remove("Pencil")
print my_set               # set(['Duster', 'Chalk', 'Pen', 'Board', 'Eraser'])

# Discard operation
my_set.discard("Pen")
print my_set               # set(['Duster', 'Chalk', 'Board', 'Eraser'])

# Difference between remove and discard : Whenever we try to remove already removed element, "remove" throws an error.
# While "discard" doesn't throw any error when we try to discard already removed element.
# my_set.remove("Pencil")    # KeyError: 'Pencil'
my_set.discard("Pen")        # Runs fine without throwing any error

# Pop operation. It removes one element randomly
my_set.pop()
print my_set               # set(['Chalk', 'Board', 'Eraser'])

# For clearing entire set
my_set.clear()
print my_set               # set([])

# For deleting set
del my_set

# Nested set
my_set2 = {"Apple", 1, 2, (3, 4, 5)}
print my_set2              # set([(3, 4, 5), 2, 'Apple', 1])

# To convert list to set
my_list = [1, 2, 3]
print my_list              # [1, 2, 3]
my_set3 = set(my_list)
print my_set3              # set([1, 2, 3])

# Mathematical operation through sets : UNION , INTERSECTION, DIFF, SYMMETRIC DIFF
A = {'A', 'B', 1, 2, 3}
B = {'B', 'C', 3, 4, 5}

# Union of A and B. Will print all the elements of A and B and will remove duplicate elements
print A.union(B)           # set(['A', 1, 2, 3, 4, 5, 'C', 'B'])
print A | B                # set(['A', 1, 2, 3, 4, 5, 'C', 'B'])

# Intersection of A and B. Will print only the elements common in both A and B set
print A.intersection(B)    # set(['B', 3])
print A & B                # set(['B', 3])

# Difference of A and B. Will print elements : A-B
print A.difference(B)      # set(['A', 1, 2])
print A - B                # set(['A', 1, 2])

# Symmetric Difference of A and B. Will print data that is unique to both A and B
print A.symmetric_difference(B)      # set(['A', 1, 'C', 4, 5, 2])
print A ^ B                          # set(['A', 1, 'C', 4, 5, 2])