def reverse_if_multiple_of_four(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string