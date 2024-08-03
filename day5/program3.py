#Add two matrices

#taking number of rows and columns
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

#initializing input matrices
matrix1 = []
matrix2 = []

#getting first matrix
print("First matrix:")
for i in range(rows):    #loop to keep track of rows
    print(f'Enter {columns} numbers of row{rows}')
    matrix_row = []      #initializing a list to store a row
    for j in range(columns):    #loop to keep track of columns
        matrix_row.append(int(input()))    #taking input and appending to row list
    matrix1.append(matrix_row)    #adding row list to make 1st matrix [list of list]
    
#getting second matrix
print("Second matrix:")
for i in range(rows):
    print(f'Enter {columns} numbers of row{rows}')
    matrix_row = []
    for j in range(columns):
        matrix_row.append(int(input()))
    matrix2.append(matrix_row)

#printing matrices
print('First matrix')
for row in matrix1:    #iterating through the rows
    for numbers in row:    #iterating through the elements in that single row
        print('%-3s'%(numbers), end='')   #printing
    print()
    
print('Second matrix')
for row in matrix2:
    for numbers in row:
        print('%-3s'%(numbers), end='')
    print()

#adding the matrices
matrix_sum = []    #initializing the matrix to store sum
for i in range(rows):
    matrix_row = []
    for j in range(columns):
        matrix_row.append(matrix1[i][j] + matrix2[i][j])    #adding the matrix elements and appending it to the sum matrix
    matrix_sum.append(matrix_row)

#printing matrix sum
print('Sum matrix')
for row in matrix_sum:
    for numbers in row:
        print('%-3s'%(numbers), end='')
    print()