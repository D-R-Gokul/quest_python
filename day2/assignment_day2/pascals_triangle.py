#print pascals triangle
from math import factorial
input_number = int(input("Enter number of lines"))
for i in range(input_number):
        value = 1
        print(" " * (input_number - i), end="")  # Center align
        for j in range(i + 1):
            print(f"{value} ", end="")
            value = value * (i - j) // (j + 1)
        print()
    