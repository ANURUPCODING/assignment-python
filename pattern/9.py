rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    number = 1
    print(" " * (rows - i), end="")

    for j in range(1, i + 1):
        print(number, end=" ")
        number = number * (i - j) // j
        

    print()
