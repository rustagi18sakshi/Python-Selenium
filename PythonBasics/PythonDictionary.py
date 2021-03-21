# Set in Python uses : {K:V}
# Unordered, indexed, changeable, No duplicates

my_dict = {
    "class" : "animal",
    "name"  : "giraffe",
    "age"   : 10
}

print my_dict                # {'age': 10, 'class': 'animal', 'name': 'giraffe'}

# For getting the value of a single key
print my_dict["name"]        # giraffe
print my_dict.get("name")    # giraffe

# To print all the keys
print my_dict.keys()         # ['age', 'class', 'name']

# To print all the values
print my_dict.values()       # [10, 'animal', 'giraffe']

# FOR loop for printing only values
for x in my_dict:
    print my_dict[x]

# Output :
# 10
# animal
# giraffe

# FOR loop for printing both key and values together
for x, y in my_dict.items():
    print x, y

# Output :
# age 10
# class animal
# name giraffe

# For updating value of a key
my_dict["name"] = "elephant"
print my_dict               # {'age': 10, 'class': 'animal', 'name': 'elephant'}

# For adding new key/value pair
my_dict["color"] = "grey"
print my_dict                # {'color': 'grey', 'age': 10, 'class': 'animal', 'name': 'elephant'}

# For deleting a key/value pair
my_dict.pop("color")
print my_dict                # {'age': 10, 'class': 'animal', 'name': 'elephant'}

# For deleting the last item in unordered dictionary
my_dict.popitem()
print my_dict                # {'class': 'animal', 'name': 'elephant'}

# Other way for deleting a key/value pair
del my_dict["class"]
print my_dict                # {'name': 'elephant'}

# For clearing entire dictionary
my_dict.clear()
print my_dict               # {}

# For deleting dictionary
del my_dict


