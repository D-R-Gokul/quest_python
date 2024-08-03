#Accept N main strings and N sub strings into lists and check create a list of numbers of 0s and 1s where 0 represents that the sub string at respective index is not a substring of the main string.

main_string = list(input("Enter the main strings separated by spaces to check the presence of substring: ").split())
sub_string = list(input("Enter the sub strings separated by spaces to check the presence in main string: ").split())
i= 0
check_result = []
if(len(main_string) == len(sub_string)):
    for i in range(len(main_string)):
        if sub_string[i] in main_string[i]:
            check_result.append(1)
        else:
            check_result.append(0)
    print(f'Result list={check_result}')
else:
    print("The main string and substring should by of same length")