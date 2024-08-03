#Accept N strings and count the number of Palindromes in it
input_string = list(input("Enter the strings separated by spaces to check number of palindromes: ").split())
# taking input string and storing as a list
count = 0  #initializing count to 0
for element in input_string:  #iterarting through the input list
    if(element == element[: : -1]):  #checking for palindrome in list elements
        print(element)
        count += 1  #increasing count by 1 if element is palindrome
print(f'There are {count} number of palindromes in the input string')  #printing count