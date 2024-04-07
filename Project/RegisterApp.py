
name = input("What is your name? ")

if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 3:
    print("Name: ", name)
