# Function
def printHello():
    print "hello"

printHello()          # hello

# Function with argument
def printHi(name):
    print "Hi, "+name

printHi("Sakshi")     # Hi, Sakshi

# Function with default value
def printHi(name="John"):
    print "Hi, "+name

printHi()             # Hi, John

# Sum Function
def sum(a,b,c):
    print(a+b+c)

sum(10,20,30)         # 60

# Sum Function with return
def returnSum(a,b,c):
    """ This is a function to calculate sum of 3 numbers """
    return(a+b+c)

x = returnSum(10,20,30)
print x                # 60

