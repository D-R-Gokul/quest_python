#Find sum of Even placed digits in a number
input_number=input("Enter the number of which the sum of digits of even place have to be found:  ")
sum_of_even=0
for i in range(len(input_number)):
    if((i+1)%2==0):
        sum_of_even += int(input_number[i])
print(f'Sum of digits in even position of {input_number} is {sum_of_even}')
