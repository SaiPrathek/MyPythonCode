# Program to print factors of given number number on the command line

import sys

if len(sys.argv) < 2:
    print("Missing Number")
    exit(1)

n = int(sys.argv[1])
for i in range(2, n // 2 + 1):
    if n % i == 0:
        print(i)
