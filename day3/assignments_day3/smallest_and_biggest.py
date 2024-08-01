#Program to find the smallest and biggest number in an array of N
input_number = int(input("Enter the number of elements you would like to have in the array:  "))
input_list =[]   #initializing a list for input
print("Enter the elements one by one: ")
for i in range(input_number):
    element = int(input())  # Read one element at a time
    input_list.append(element)  # Add the element to the list
    
input_list.sort()  #sorting the list

print(f'The smallest number in array is {input_list[0]} and largest number is {input_list[len(input_list)-1]}')         
2#printing first and last element of sorted array to get the smallest and largest element 