# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
string = "string"

# if the length of the string is less than 3, leave it unchanged
if len(string) < 3:
    result = string
# if the string already ends with 'ing', add 'ly' instead
elif string.endswith("ing"):
    result = string + "ly"
# otherwise, add 'ing' at the end of the string
else:
    result = string + "ing"

# print the resulting string
print(result)