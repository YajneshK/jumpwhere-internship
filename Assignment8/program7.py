class StringReverser:
    def __init__(self):
        pass
    
    def reverse_words(self, string):
        # Split the string into words using the space character as a separator
        words = string.split()
        
        # Reverse the order of the words
        words.reverse()
        
        # Join the words into a single string with space characters in between
        reversed_string = ' '.join(words)
        
        return reversed_string