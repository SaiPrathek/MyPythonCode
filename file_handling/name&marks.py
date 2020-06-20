# Program to read names and marks from file and display sum of marks

with open("names.txt", "rt") as f:
    name = f.readlines()

new = []
for i in range(len(name)):
    new.append(name[i].split(","))


def s(lst):
    add = 0
    for j in range(1, len(lst)):
        try:
            add += int(lst[j])
        except Exception as ex:
            pass
            # print(f"Error - {ex}")
    return add


for k in range(len(new)):
    print(new[k][0].ljust(8), "-", s(new[k]))

new.sort()
print()

for k in range(len(new)):
    print(new[k][0].ljust(8), "-", s(new[k]))

d = {new[l][0]: s(new[l]) for l in range(len(new))}
print()

for i in sorted(d, key=d.get, reverse=True):
    print(i.ljust(8), "-", d[i])
