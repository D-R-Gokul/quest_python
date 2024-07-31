#Program to count the number of digits in a number
input_number=int(input("Enter the number to count the number of digits: "))
count=0
while(input_number>0):
    count=count+1
    input_number=int(input_number/10)
print("The number of digits in the entered number is "+str(count))