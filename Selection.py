import os

print("Welcome to the Modular Script Manager.")
print("Please select 'y' or 'n' to add or exclude a script to the script pool.")
ls = os.listdir()
files = []


def pool():
    for x in ls:
        print("Would you like to add " + x + " to the pool?")
        y = input()
        while True:
            if y == "n":
                print(x + " was not added to the pool")
                break
            elif y == "y":
                print(x + " was added to the pool")
                files.append(x)
                break
            else:
                print("Invalid Input, Try again.")
                y = input()
                pass


pool()


def check():
    print("The files you have chosen are " + str(files) + "is this correct?")
    y = input()
    while y == "n":
        if y == "n":
            print("Please try again")
            pool()
            check()
            break
        elif y == "y":
            with open('Execute.py', 'w') as outfile:
                for names in files:
                    with open(names) as infile:
                        outfile.write(infile.read())
                    outfile.write("\n")
                    print("All of the scripts selected have been compiled")


check()
