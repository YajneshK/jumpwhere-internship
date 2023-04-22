starts_with = lambda x: lambda y: y.startswith(x)

string = "hello world"
char = "h"
result = starts_with(char)(string)
print(result) # Output: True
True