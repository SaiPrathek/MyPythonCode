# Program to sort names in phones.txt

phones = {}
with open("phones.txt", "rt") as r:
    for line in r:
        parts = line.split(",")
        print(parts)
        if len(parts) != 2:
            continue
        if parts[1].strip("\n").isdigit():
            phones[parts[0]] = parts[1].strip("\n")
        else:
            with open("bad_data.txt", "at") as w:
                w.write(f"{parts[0]},{parts[1]}")
#
# for name, phone in sorted(phones.items()):
#     print(name.ljust(10), phone)
