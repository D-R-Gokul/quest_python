#lower case to upper case
print("Enter a character")
character = input()
if('a'<= character <= 'z'):
    upper_case = chr(ord(character)-32)
    print('upper case of '+character+'is '+upper_case)
else:
    print("Invalid input")