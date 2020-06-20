# Program to print factors of all given number number on the command line

import sys

if len(sys.argv) < 2:
    print("Missing Number")
    exit(1)

factors = set()


def cf(*n):
    for j in range(len(n) - 1):
        for i in range(2, n[j] + 1):
            if n[j] % i == n[j + 1] % i == 0:
                factors.add(i)
    return factors


for j in range(1, len(sys.argv) - 1):
    a = int(sys.argv[j])
    b = int(sys.argv[j + 1])
    cf(a, b)

print(factors)
