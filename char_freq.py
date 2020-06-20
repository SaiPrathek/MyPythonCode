# Program to calculate character frequency in the given string

d = {}
s = input("Enter The String : ")

for i in range(len(s)):
    if s[i] not in d:
        d[s[i]] = s.count(s[i])

for i in sorted(d):
    print(i, d[i])

print(d)

for i in range(10):
    print("how do you like me now")

n = [n for n in range(10)]
