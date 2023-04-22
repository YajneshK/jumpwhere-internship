class StringManipulator:
    def __init__(self):
        self.string = ""
    
    def get_string(self):
        self.string = input("Enter a string: ")
    
    def print_string(self):
        reversed_string = self.string[::-1]
        print("Reversed string: ", reversed_string)