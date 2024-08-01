#program to remove negative numbers in a list
input_numbers = list(map(int,input("Enter numbers separated by ' ': ").split()))  #taking input from user
print (f'Entered numbers {input_numbers}')  #printing input
# Remove negative numbers using list comprehension
input_numbers = [number for number in input_numbers if number >= 0]  
#printing list after removing
print(f'After removing negative numbers {input_numbers}')