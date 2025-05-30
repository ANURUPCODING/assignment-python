string = input("Enter a string: ")
reversed = string[::-1]


if string == reversed:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
