#Count the number of Prime digits in a number
input_number = input("Enter a number to find its second largest digit:  ")
number = [int(char) for char in input_number]
count = 0
for i in range(len(number)):
    if(number[i])