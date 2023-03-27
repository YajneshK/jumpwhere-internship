#Write a Python program to count the number of characters (character frequency) in a string. 
#Sample String : google.com'

string = "google.com"

char_freq = {}

for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print(char_freq)