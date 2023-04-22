tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_tuples = sorted(tuples, key=lambda x: x[1])

print("Original list of tuples:", tuples)
print("Sorting the List of Tuples:", sorted_tuples)