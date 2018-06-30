from mylib import *

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

def save_file():
    try:
        f = open("compass_code.js", "a")
        # f = open("compass_code.js", "a") # OS does not care if you open it twice
        f.write("console.log('Hello from Python')\n")
        f.write("console.log('Python is amazing')\n")
        f.close()
    except Exception:
        print("Could not save file")

save_file()

def read_file():
    try:
        f = open("./pnrcreate/pnrCreateMain.js", "r")
        for codeline in f.readlines():
            print(codeline)
        f.close()
    except Exception:
        print("Could not read from file")

read_file()

# /Users/v738110/Compass/GitHub/ui/app/Shopping/ShoppingUI/CCShopping/AMD/js/pnrcreate
