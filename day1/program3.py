#Check the number is a perfect square or not
import math
print("Enter a number to check if it is Perfect Square")
input_number = int(input())                         #taking the input
root_number = int(math.sqrt(input_number))          #finding the root and type casting it to int
root_number_square = root_number*root_number        #multiplying root whit the root itself
if(root_number_square*root_number_square == input_number):  #checking if the product is same as the input
    print("Is a Perfect square")
else:
    print("Not a perfect square")