is_number = lambda s: s.replace('.', '', 1).isdigit()

string1 = "1234"
string2 = "12.34"
string3 = "abc"

result1 = is_number(string1)
result2 = is_number(string2)
result3 = is_number(string3)

print(result1) # Output: True
print(result2) # Output: True
print(result3) # Output: False