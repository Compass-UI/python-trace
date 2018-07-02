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



def save_file():
    try:
        f = open("compass_code.js", "a")
        # f = open("compass_code.js", "a") # OS does not care if you open it twice
        f.write("console.log('Hello from Python')\n")
        f.write("console.log('Python is amazing')\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("./pnrcreate/pnrCreateMain.js", "r")
        for codeline in f.readlines():
            print(codeline)
        f.close()
    except Exception:
        print("Could not read from file")

# 