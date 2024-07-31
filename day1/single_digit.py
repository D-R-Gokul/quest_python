#Checking whether the number is single digit or not
input_number= int(input("Enter a number:  "))   #taking input from user and type casting it to integer
if(0<= input_number< 10):                       #checking if the number is in the range 0-10
    print(str(input_number)+ " is single digit") #if yes printing single digit
else:
    print(str(input_number)+" is not single digit")  #if no printing not single digit