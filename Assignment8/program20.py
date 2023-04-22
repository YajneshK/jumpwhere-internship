original_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
sorted_list = sorted(original_list, key=lambda x: (isinstance(x, int), x))
print("Original list:", original_list)
print("Sorted list:", sorted_list)