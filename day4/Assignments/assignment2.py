# Accpet a string of space seperated numbers and store them as a matrix (list of lists) of n rows.
# Now print the matrix row-wise

input_number = int(input("Enter the number of rows you would like to have: "))
matrix = []
i = 1
while i <= input_number :
    matrix.append(list(map(int, input(f'Enter the row{i}: ').split())))
    i += 1
for row in matrix:
    print(row)
print(matrix)