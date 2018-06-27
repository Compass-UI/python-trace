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