#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.string1 = "abc"
string1 = "abc"
string2 = "xyz"

# swap the first two characters of each string
new_string1 = string2[:2] + string1[2:]
new_string2 = string1[:2] + string2[2:]

# concatenate the two strings with a space in between
result = new_string1 + " " + new_string2

# print the resulting string
print(result)