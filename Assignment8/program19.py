lst = ['red', 'black', 'white', 'green', 'orange']
substr = 'ack'

result = list(filter(lambda x: substr in x, lst))

print("Original list:", lst)
print("Substring to search:", substr)
print("Elements of the said list that contain the specific substring:", result)