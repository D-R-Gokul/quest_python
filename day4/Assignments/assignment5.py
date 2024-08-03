#Accept N main strings and N sub strings into lists and check create a list of numbers of 0s and 1s where 0 represents that the sub string at respective index is not a substring of the main string.


#taking main and substrings and storing as list
main_string = list(input("Enter the main strings separated by spaces to check the presence of substring: ").split())
sub_string = list(input("Enter the sub strings separated by spaces to check the presence in main string: ").split())

i= 0
check_result = []    #initializing a list to store result
if(len(main_string) == len(sub_string)):    #checking if the main and sub string list have same length
    for i in range(len(main_string)):    #iterating through elements main string
        if sub_string[i] in main_string[i]:   #checking if substring of same index is present at main string
            check_result.append(1)    #if present adding 1 to result list
        else:
            check_result.append(0)    #if no adding 0 to result list
    print(f'Result list={check_result}')    #printing result
else:
    print("The main string and substring should by of same length")