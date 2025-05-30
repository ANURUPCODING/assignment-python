string = input("Enter a string: ")

words = string.split()
largest_word = ""

for word in words:
    if len(word) > len(largest_word):
        largest_word = word

print("The largest word is:", largest_word)
