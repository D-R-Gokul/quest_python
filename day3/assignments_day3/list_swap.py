#Accepting N numbers from the user and swap the consecutive elements
number_of_elements = int(input("Enter the number of elements you would like to have in the array:  "))
input_list = []
print("Enter the elements one by one: ")
for i in range(number_of_elements):
    element = int(input())  # Read one element at a time
    input_list.append(element)  # Add the element to the list

print(f'Before swapping {input_list}')  #printing the list
for i in range(0,len(input_list),2):
    if i < len(input_list)-1:
        temp = input_list[i]
        input_list[i] = input_list[i+1]
        input_list[i+1] = temp
print(f'After swapping{input_list}')