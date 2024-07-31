#Program to find the number of odd digits in a number
input_number=int(input("Enter a number to count the number of odd numbers in it: "))
count=0
temp_number= input_number
while(temp_number>0):
    r=temp_number%10
    if(r%2 != 0):
        count+=1 
    temp_number=temp_number//10
    
    
print(f'There are {count} odd numbers in {input_number}')