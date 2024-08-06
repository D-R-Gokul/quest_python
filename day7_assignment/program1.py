#exception handling
input1 =input("Enter a value: ")
input2 = input("Enter a value2: ")
try: 
    input1 =int(input1)
    input2 = int(input2)
    print(input1 + input2)
except ValueError:
    
    if(isinstance(input1, str) == isinstance(input2, str)):
        print(" ".join([input1,input2]))
    else:
        print("Type error occured: You cant add an integer to a string")