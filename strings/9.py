string = input("Enter a string: ")

words = string.split()
updated = ""

for word in words:
    capitalized = word.capitalize()
    updated += capitalized + " "


print("Capitalized string:", updated)
