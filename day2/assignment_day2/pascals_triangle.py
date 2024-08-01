#print pascals triangle
from math import factorial
input_number = int(input("Enter number of lines"))
for i in range (input_number):
    for j in range(input_number-i+1):
        print(end=' ')
    