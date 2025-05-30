num = int(input("Enter a number: "))
original= num
sum = 0
n = len(str(num))

while num > 0:
    digit = num % 10
    sum += digit ** n
    num //= 10

if original == sum:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")
    
    
    
    # to the power ke liye **