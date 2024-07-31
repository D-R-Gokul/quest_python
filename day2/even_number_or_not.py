#program to check whether the number entered is even or not
print("Enter the number")
number=int(input())                      #taking input from user and explicitly type casting it to int
if(number%2==0):                         #checking whether the number is even (if a number%2== 0 then the number is even)
    print(str(number)+' is even')
else:                                    #if the number is not even else part prints the message
    print(str(number)+' is not even')