#Program to print X shape inside a hollow Square
 
print('Program to print X shape inside Hollow Square')
number_of_lines = int(input('Enter the number of lines: '))    #getting user input and storing as integer
for i in range(number_of_lines):                    #outer for loop for rows
    for j in range(number_of_lines):                #inner for loop for columns
        if i == 0 or i == number_of_lines-1 or j == 0 or j == number_of_lines-1 or i == j or j == number_of_lines-i-1:                       #checking the conditions where star has to be print
            print('*', end=' ')                    #printing star
        else:
            print(' ', end=' ')                    #printing space
    print()