#Phonebook

name = ""
number = 0
phonebook = {name: number}
del phonebook[""]

def addName(name, number):
    phonebook.update({name: number})
    print("Added: " + name + ": " + number)

def delName(name):
    del phonebook[name]

def findName(name):
    find = phonebook.get(name)
    findtring = str(find)
    if find == None:
        print("Name " + name + " not found!")
    else:
        print(name + ": " + findtring)
    
def launch():
    print("phonebook manager")
    print("Available commands: add, find, del, exit")
    while True:
        command = input("What would you like to do? ")
        if command == "exit":
            break
        if command == "add":
            name, number = input("Give name and number you want to add: ").split()
            addName(name, number)
        if command == "del":
            name = input("Give name you want to delete: ")
            delName(name)
        if command == "find":
            name = input("Give name you want to find: ")
            findName(name)

launch()
