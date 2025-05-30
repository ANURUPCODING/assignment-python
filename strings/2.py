string = input("Enter a string: ")
vowels = consonants = digits = white_spaces = others = 0
vowel_chars = "aeiouAEIOU"

for char in string:
    if char in vowel_chars:
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        white_spaces += 1
    else:
        others += 1


print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("White spaces:", white_spaces)
print("Other characters (special symbols):", others)
