#Print a hollow square of n lines
number = int(input("Enter the number of lines required for the square:  "))
for i in range(number):
    for j in range(number):
        if i == 0 or i == number-1 or j == 0 or j == number-1:
                print('*', end=' ')
        else:
                print(' ', end=' ')
    print()