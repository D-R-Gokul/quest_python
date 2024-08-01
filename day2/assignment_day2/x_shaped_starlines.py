#Print X shape made up of stars of n lines
number_of_lines = int(input("Enter the number of lines for X:  "))
for i in range (number_of_lines):
    for j in range(number_of_lines):
        if(i ==j or i+j == number_of_lines-1):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()