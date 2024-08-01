#Count the number of Prime digits in a number
input_number = input("Enter a number to find its second largest digit:  ")
prime_number = [2,3,5,7]
count = 0
for digit in input_number:
    if int(digit) in prime_number:
        count +=1
        
print(f'There are {count} number of prime numbers in {input_number}')