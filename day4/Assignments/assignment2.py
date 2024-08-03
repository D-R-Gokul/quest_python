# Accpet a string of space seperated numbers and store them as a matrix (list of lists) of n rows.
# Now print the matrix row-wise

input_number = int(input("Enter the number of rows you would like to have: ")) #taking number of rows from user
matrix = []  #initializing a list for matrix
i = 1
while i <= input_number :  #loop to maintain the number of rows
    matrix.append(list(map(int, input(f'Enter the row{i}: ').split()))) # taking input row and adding it to matrix
    i += 1
for row in matrix:  #iterating through matrix[]
    print(row)  #printing each row
print(matrix)