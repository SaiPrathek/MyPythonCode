# Program to print factors of all given number number on the command line

import sys

if len(sys.argv) < 2:
    print("Missing Number")
    exit(1)
factors = {}
for j in range(1, len(sys.argv)):
    n = int(sys.argv[j])
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            if i not in factors:
                factors[i] = 1
            else:
                factors[i] += 1

print(factors)

for k in factors.keys():
    if factors[k] == len(sys.argv) - 1:
        print(k)
