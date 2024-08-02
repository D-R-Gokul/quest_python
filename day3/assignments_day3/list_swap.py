#Accepting N numbers from the user and swap the consecutive elements
input_list = list(map(int,input("Enter numbers separated by ' ': ").split()))  #taking input from user

print(f'Before swapping {input_list}')  #printing the list
for i in range(0,len(input_list),2): #iterating through the loop
    if i < len(input_list)-1:       #ensuring i is within the range 
        temp = input_list[i]        #swapping
        input_list[i] = input_list[i+1]
        input_list[i+1] = temp
print(f'After swapping{input_list}')