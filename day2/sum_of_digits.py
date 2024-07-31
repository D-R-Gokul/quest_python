#program to find the sum of digits in the number

input_number=int(input("Enter a number to count the number of odd numbers in it: "))
sum_of_digits = 0
temp_number = input_number
while(temp_number>0):
    r = temp_number %10
    sum_of_digits += r
    temp_number=temp_number//10
    
    
print(f'The sum of digits in {input_number} is {sum_of_digits}')