#Program to find the number of odd digits in a number
input_number=int(input("Enter a number to count the number of odd numbers in it: "))
count=0
while(input_number>0):
    r=input_number%10
    if(r%2 == 0):
        count=count+1
    input_number=int(input_number/10)
    
    
print("There are "+str(count)+" in the number entered")