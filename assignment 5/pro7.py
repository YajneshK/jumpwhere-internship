string1 = "The lyrics is not that poor!"
string2 = "The lyrics is poor!"

# find the positions of 'not' and 'poor' in the string
not_index = string1.find("not")
poor_index = string1.find("poor")

# if 'not' appears before 'poor' and both substrings are present in the string, replace 'not...poor' with 'good'
if not_index < poor_index and not_index != -1 and poor_index != -1:
    result = string1[:not_index] + "good" + string1[poor_index+4:]
# otherwise, leave the string as it is
else:
    result = string1

# find the positions of 'not' and 'poor' in the string
not_index = string2.find("not")
poor_index = string2.find("poor")

# if 'not' appears before 'poor' and both substrings are present in the string, replace 'not...poor' with 'good'
if not_index < poor_index and not_index != -1 and poor_index != -1:
    result2 = string2[:not_index] + "good" + string2[poor_index+4:]
# otherwise, leave the string as it is
else:
    result2 = string2

# print the resulting strings
print(result)
print(result2)