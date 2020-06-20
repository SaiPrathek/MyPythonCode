# Program to accept 10 inputs and print the sum of the numbers
n = []
for i in range(10):
    try:
        n.append(int(input("Enter The Number : ")))

    except Exception as ex:
        print(ex)

print(sum(n))
