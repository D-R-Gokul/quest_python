#Program to find the biggest digit in the number
input_number = input("Enter a number to find the biggest digit in it:  ")
biggest_digit=0
for digit in input_number:
    if(int(digit) > biggest_digit):
        biggest_digit = int(digit)
    
print(f'Biggest digit in {input_number} is {biggest_digit}')