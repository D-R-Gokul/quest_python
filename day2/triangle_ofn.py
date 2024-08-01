'''
Program to accept number of lines of the Triangle and draw the Trianlge:
*
**
***
****
*****
'''

line_number = int(input("Enter the number of lines required for the triangle:  ")) #getting the input 
for i in range(line_number + 1):   #iterating to keep the count of lines
    print('*' * i)    #printing *