import sys

num = int(sys.argv[1])


def fun(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


print(fun(num))
if __name__ == "__main__":
    print(f"Running Main")
else:
    print(f"Importing Factorial")


