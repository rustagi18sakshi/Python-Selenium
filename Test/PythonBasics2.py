# Loops in Python

# IF Statement
if 5 > 3:
    print "5 is greater than 3"

# IF-ELIF-ELSE Statement
num = 3

if num > 0:
    print "This is a positive number"
elif num == 0:
    print "Number is zero"
else:
    print "This is a negative number"

# FOR Loop Number
num = [1, 2, 3, 4, 5]      # List in python

for val in num:
    print val

# Output :
# 1
# 2
# 3
# 4
# 5

# FOR Loop Sum
num = [10, 20, 13, 4, 5]
sum = 0

for val in num:
    sum = sum + val

print "Total is :", sum          # Total is : 52

# FOR Loop String
fruits = ["apple", "orange", "grapes"]

for val in fruits:
    print val
else:
    print "No fruits left"

# Output :
# apple
# orange
# grapes
# No fruits left

# WHILE Loop
i = 1
num = 10
sum = 0

while i < num:
    sum = sum + i
    i = i + 1
print "Total sum is :", sum       # Total sum is : 45

# WHILE Loop with raw_input
print "Enter a number : "
num = int(raw_input())     # For number input, cast it to int
i = 1
sum = 0

while i < num:
    sum = sum + i
    i = i + 1
print "Total sum is :", sum

# Output :
# Enter a number :
# 7
# Total sum is : 21
