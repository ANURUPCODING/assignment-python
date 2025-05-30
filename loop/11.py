base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1
count = 0

while count < exponent:
    result = result * base
    count = count + 1

print(f"{base} raised to the power {exponent} is {result}")
