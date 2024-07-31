
#checking whether the number input is even or not
print("Enter the number")
input_number=int(input())                   #taking the input and type casting it to int
if(input_number%2==0):                      #checking if the number is even
    print(str(input_number)+' is even')     #printing even if the number is even
else:
    print(str(input_number)+' is not even') #else printing the number is not even