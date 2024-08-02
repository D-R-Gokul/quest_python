#Accept N strings and count the number of Palindromes in it
input_string = list(input("Enter the strings separated by spaces to check number of palindromes: ").split())
# print(input_string)
count = 0
for element in input_string:
    if(element == element[: : -1]):
        print(element)
        count += 1
print(f'There are {count} number of palindromes in the input string')