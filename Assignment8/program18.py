check_string = lambda s: len(s) >= 10 and any(c.isupper() for c in s) and any(c.islower() for c in s) and any(c.isdigit() for c in s)

s = 'PaceWisd0m'
if check_string(s):
    print('valid string')
else:
    print('invalid string')