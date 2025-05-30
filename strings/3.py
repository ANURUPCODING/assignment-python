string = input("Enter the string : ")
result = ""

for char in string:
    if char.isalpha():
        result = result+char

print(f"Update string with only alphabets is '{result}' ")
