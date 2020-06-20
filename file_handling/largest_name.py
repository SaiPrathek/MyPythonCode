# Program to find and display the name with largest length

with open("names.txt", "rt") as f:
    names = f.readlines()

for m in range(len(names)):
    names[m] = names[m].split(",")

new = []
for i in names:
    new.append(i[0])

print(max(new, key=len))
