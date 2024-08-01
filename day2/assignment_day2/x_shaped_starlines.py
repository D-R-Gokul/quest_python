#Print X shape made up of stars of n lines
number_of_lines = int(input("Enter the number of lines for X:  ")) #input from user
if (number_of_lines % 2==0):
    print('Even numbers cannot give the perfect X shape')
    
else: 
    for i in range (number_of_lines):          #outer for loop for rows
        for j in range(number_of_lines):       #inner for loop for columns
            if(i ==j or i+j == number_of_lines-1):
                print('*', end=' ')
            else:
                print(' ',end=' ')
        print()