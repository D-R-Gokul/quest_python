#Accept N strings, and check how many of them possess the string X


# entering main strings and storing as list
input_string = list(input("Enter the main strings separated by spaces to check the presence of substring: ").split())

# entering sub strings and storing as list
input_sub_string = input("Enter the substring you need to check: ")  
count = 0    #initializing count as 0
#iterating through the elements of main string
for element in input_string:     
    #checking if sub string is present in the main string 
    if input_sub_string in element:    
        print(element)
        count += 1    #if yes increasing count by 1
print(f'There are {count} number of input string ')