# Program to print factors of all given number number on the command line

import sys

if len(sys.argv) < 2:
    print("Missing Number")
    exit(1)

for j in range(1, len(sys.argv)):
    print()
    n = int(sys.argv[j])
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print(i)
