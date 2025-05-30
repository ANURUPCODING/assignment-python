string = input("Enter a string: ")
result = ""

for char in string:
    if char.isalpha():
        if char == 'z':
            result += 'a'
        elif char == 'Z':
            result += 'A'
        else:
            # ord is used to convert from char to ascii and chr to convert ascii to char
            result += chr(ord(char) + 1)

    else:
        result += char

print("Modified string:", result)
