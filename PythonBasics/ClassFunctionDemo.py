# Defining Class in Python
import time

class MyClass:

    # Defining variable in class
    name = "Sakshi"

    # The init method is similar to constructors in C++ and Java.
    def __init__(self, employeeName, age):
        self.employeeName = employeeName
        self.age = age

    # Every function in a class will have first argument as self. We can rename it also.
    def sum(self, a, b):
        print a+b

# Access the class by declaring object x here
x = MyClass("Shruti",30)
print x.name         # Sakshi
x.sum(5, 4)          # 9

# Accessing variables of self
print x.employeeName     # Shruti
print x.age              # 30

time.sleep(1)

# Deleting object x
del x

# Trying to access variable after deleting x and expecting error
print x.name             # NameError: name 'x' is not defined
