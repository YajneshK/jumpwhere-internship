def uppercase_if_two_uppercase_chars(string):
    uppercase_count = 0
    for i in range(4):
        if string[i].isupper():
            uppercase_count += 1
    if uppercase_count >= 2:
        return string.upper()
    else:
        return string