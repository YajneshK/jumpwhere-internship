string = 'thequickbrownfoxjumpsoverthelazydog'
char_count = {}

# Count the occurrence of each character in the string
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the characters that occur more than once with their count
for char in char_count:
    if char_count[char] > 1:
        print(char, char_count[char])