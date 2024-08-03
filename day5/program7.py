
number_of_rows = int(input("Enter the number of rows in array: "))
grid_array = []

#getting the grid values
for i in range(number_of_rows):
    row = []
    print(f"Enter the values of row {i+1}")
    for j in range(2):
        row.append(int(input()))
    grid_array.append(row)

print()
for row in grid_array:
    for number in row:
        print('%-4s'%(number), end='')
    print()

#calculating the maximum sum
maximum_element_sum = max(grid_array[0])
for i in range(1, number_of_rows):
    if(max(grid_array[i]) > max(grid_array[i-1])):
        maximum_element_sum += max(grid_array[i])

print(f'Maximum values gained is {maximum_element_sum}')



# # Find the maximum possible total sum of values in all cells he can visit on his path
 
# rows_of_grid = int(input('Enter number of rows of the Matrix: '))
# columns = 2
 
# matrix1 = []
 
# # Now let us read elements of matrix
# for i in range(rows_of_grid):
#     print(f'Enter {columns} numbers of Row-{i+1}')
#     row_numbers = [] # List that stores numbers of a specific row
#     for j in range(columns): # To read numbers of a row
#         row_numbers.append(int(input()))
#     matrix1.append(row_numbers)
 
# # Now let us print the matrix
# print("The given grid is: ")
# for row in matrix1:
#     for number in row:
#         print('%-3s'%(number), end='')
#     print()
 
# sum_of_max_elements = max(matrix1[0])
# previous_max_element = max(matrix1[0])
 
# for i in range(1,len(matrix1)):
#     current_max_element = max(matrix1[i])
#     if current_max_element > previous_max_element:
#         sum_of_max_elements += current_max_element
#         previous_element = current_max_element
#     else:
#         break
# print("The maximum possible sum of values in all the cells he can visit is = ",sum_of_max_elements)