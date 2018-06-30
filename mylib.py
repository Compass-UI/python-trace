a = [
    {"fname": "David", "lname": "Shams", "role": "Solution Architect" },
    {"fname": "Mike", "lname": "Knott", "role": "Solution Architect" },
    {"fname": "Bob", "lname": "Smith", "role": "Developer" }
]

def display(a):
    
    def buildmsg(e):
        return ("Mr. {0} is a {1}".format(e["fname"], e["role"]))

    for e in a:
        print(buildmsg(e))



