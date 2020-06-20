# Program to accept 10 inputs and print the sum of the numbers
n = []
while len(n) < 10:
    try:
        n.append(int(input("Enter The Number : ")))

    except Exception as ex:
        print("Invalid Number")

print(sum(n))
