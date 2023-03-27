def remove_nth_char(string, n):
    if n < 0 or n >= len(string):
        return string
    return string[:n] + string[n+1:]