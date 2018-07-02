from mylib import *

import numpy as np

# Functions 
def add_nums(a,b):
    return a + b

# Strings
print("""Documentation""");
print("capitalize".capitalize());
print("hello".replace("e", "a"));
print("hello".isalpha());
print("123".isdigit()); #Check before converting
print("some, cvs, values".split(","));
name = "David"
message = "Hello"
print("{1} {0}".format(name, message));
true = True
false = False
print(int(true))
print(int(false))

# Sets

# Tuples

# Frozen Sets

print(add_nums(2,3));

# Truthy Falsy
number = 5
if number:
    print("Number {0} is defined".format(number))

no = None
if no:
    print("no is not false")
else:
    print("no is false")

if not no:
    print("You said yes.")

# Ternary
a = 1
b = 2
"bigger" if a > 2 else "smaller"

# List comprehension
names = ["David", "Sean", "Abel", "Jacob"]
print(names[0])
print(names.append("Tia"))
print(names[len(names) - 1])
print(names.append("REMOVE"))
print(names.append("REMOVE"))
print(names)
del names[len(names)-1]
del names[len(names)-1]
print(names)
print("Kids: ")
print(names[1:]) # Skip first give the rest
print(names[1:-1]) # Skip first and last and give the rest
print(names.reverse())

for name in names:
    print("Name is: {0}".format(name))

x = 0
for index in range(10): # range takes a value and converts it to a list
    x += 10
    print(x)

# display(a);

# READING WRITING TO FILES
# save_file()

# read_file()

# /Users/v738110/Compass/GitHub/ui/app/Shopping/ShoppingUI/CCShopping/AMD/js/pnrcreate

# List in Python is JavaScript array lol!

my_list = [1,2,3,4]

my_array = np.array(my_list)

print(my_array)
# print(array([1,2,3,4]))

# Generator function
line_count = 0
def read_file():
    try:
        f = open("./pnrcreate/pnrCreateMain.js", "r")
        for codeline in red_lines(f):
            print(codeline)
            print(line_count, ": ***************************************************************")
            # line_count = line_count + 1
        f.close()
    except Exception:
        print("Could not read from file")

def red_lines(f):
    for line in f:
        yield line

# read_file()

# Lambda = functions

def double(x):
    return x * 2

print(double(2))

fn = lambda x: x * 2 # Lambda version of double(x)

print(fn(3))
