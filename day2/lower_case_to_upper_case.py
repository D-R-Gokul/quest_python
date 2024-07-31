#lower case to upper case
print("Enter a character")      
character = input()                            #taking the input from user
if('a'<= character <= 'z'):                    #checking whether the letter is a lower case 
    upper_case = chr(ord(character)-32)        #subtracting 32 from the ASCII number of the letter to get its ASCII code for upper case
    print('upper case of ' +character+'is '+upper_case)  #printing the upper case
else:
    print("Invalid input")                     #if letter entered is a upper case or other invalid options