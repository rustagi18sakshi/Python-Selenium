print "'Hello World"

# Variable name is case sensitive , letters(a-z), underscore, numbers(0-9)
x = 5
y = "Automation"

print x        # 5
print y        # Automation

# Concatenation
print "Hello "+y       # Hello Automation

# Sum of two numbers
x = 10
y = 20
print x+y      # 30

# Indentation
if 10>5:
    print "10 is greater than 5"

# Function
def sum(a,b):
    print "Sum of the numbers are :", a+b       # Use comma(,) other with plus(+) you get error - TypeError: cannot concatenate 'str' and 'int' objects

m = sum(20,30)         # Sum of the numbers are : 50

# If you want to comment something use : CTRL followed by forward slash(/)

# Type of operators
x = 5
y = 2.5
z = 4j

print type(x)   # <type 'int'>
print type(y)   # <type 'float'>
print type(z)   # <type 'complex'>

# Casting
x = int(2)      # 2
y = int(2.5)    # 2
z = float(1)    # 1.0
p = str(10)     # "10"

print x
print y
print z
print p
print type(p)   # <type 'str'>

# String index operations. Index starts from 0
x = "Hello World .."

print x[1]     # e
print x[6:11]  # World

# Length of string
print len(x)    # 14

# Convert to lower and upper case
print x.lower()       # hello world ..
print x.upper()       # HELLO WORLD ..

# Strip to remove spaces at the start and end of the string
x = "  Hello World ..  "
print x.strip()        # Hello World ..

# Replace a character in a string
x = "Hello World .."
print x.replace("e","a")     # Hallo World ..

# Split the string
x = "Hello, World.."
print x.split(",")        # ['Hello', ' World..']

# Take input from user
print("Enter your name : ")
x = raw_input()         # For python 2 use raw_input(), for python 3 we can use input()
print "Hello, "+x

