# Program to accept names from user until end is entered

names = set()

while True:
    name = input("Enter The Name [end to stop] : ")
    if name == "end":
        break
    names.add(name)

with open("names.txt", "wt") as f:
    for i in sorted(names):
        f.write(f"{i}\n")
