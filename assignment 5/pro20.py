string = input("Enter a string: ")

# Initialize an empty string for the output
output = ""

# Loop through each character in the string
for i in range(len(string)):
    # If the current character is not equal to the next character, add it to the output string
    if i == len(string) - 1 or string[i] != string[i+1]:
        output += string[i]

# Print the output string
print("Output string:", output)
