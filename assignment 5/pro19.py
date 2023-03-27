string = input("Enter a string: ")
words = string.split()  # split the string into a list of words

# Initialize the smallest and largest words with the first word
smallest = largest = words[0]

# Loop through each word in the list
for word in words:
    if len(word) < len(smallest):
        smallest = word
    elif len(word) > len(largest):
        largest = word

# Print the smallest and largest words
print("Smallest word:", smallest)
print("Largest word:", largest)