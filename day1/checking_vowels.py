#checking the letter entered is a vowel or not
#print("Enter a letter to check whether it is vowel or not: ")
letter = input("Enter a letter to check whether it is vowel or not:  ")  #taking input letter user 
vowels = "aeiouAEIOU"             #String with all the vowels to check if the letter is present in this string
if letter in vowels:            #checks whether the input letter is present in the string of vowels
    print(letter+ " is a vowel")
else:
    print(letter+" is a consonant")
