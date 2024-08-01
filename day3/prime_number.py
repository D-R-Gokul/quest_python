#program to check prime number
import math             #ceil() and sqrt() are in math module
input_number = int(input("Enter a number to check it is prime or not:  ")) #getting input from user
prime = True               #Assuming the number is prime
for i in range(2,math.ceil(math.sqrt(input_number)+1)):    #for loop to iterate till ceil(sqrt(input))
    if(input_number %i ==0):         #checking divisibility of input with each number
        prime = False                 #if divisible setting prime to false
if(prime == True):                    #checking prime or not
    print(f'{input_number} is prime')
else:
    print(f'{input_number} is not prime')


