#Accept N strings, and check how many of them possess the string X
input_string = list(input("Enter the main strings separated by spaces to check the presence of substring: ").split())
# print(input_string)
input_sub_string = input("Enter the substring you need to check: ")
count = 0
for element in input_string:
    if input_sub_string in element:
        print(element)
        count += 1
print(f'There are {count} number of input string ')