matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print("Original Matrix:", matrix)

sorted_matrix = sorted(matrix, key=lambda row: sum(row))
print("Sorted Matrix in Ascending Order according to the Sum of its Rows:", sorted_matrix)

matrix = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print("Original Matrix:", matrix)

sorted_matrix = sorted(matrix, key=lambda row: sum(row))
print("Sorted Matrix in Ascending Order according to the Sum of its Rows:", sorted_matrix)