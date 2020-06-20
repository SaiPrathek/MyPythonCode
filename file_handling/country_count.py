# Program to display count of countries in country.txt

freq = {}
with open("country.txt", "rt") as r:
    countries = r.readlines()
    for i in countries:
        if i.strip("\n") in freq:
            freq[i.strip("\n")] += 1
        else:
            freq[i.strip("\n")] = 1

for j in freq:
    print(j.ljust(10), freq[j])
