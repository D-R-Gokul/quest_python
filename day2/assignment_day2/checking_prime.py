#Program to check a number is prime or not

input_number= int(input("Enter a number to check if it is prime number or not:  "))
count =0
if(input_number <=1):
    print('The entered number is neither prime nor composite')
else:
    for i in range(1,input_number+1):
        if(input_number%i == 0):
            count+=1
    if(count > 2):
        print(f'{input_number} is not prime')
    else:
        print(f'{input_number} is prime')