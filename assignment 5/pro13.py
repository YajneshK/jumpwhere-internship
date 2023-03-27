string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")

if string.startswith(prefix):
    print("The string starts with the specified prefix.")
else:
    print("The string does not start with the specified prefix.")