#Program to find second largest digit in a number
input_number = input("Enter a number to find its second largest digit:  ")
number= [int(char) for char in input_number]
sorted_numbers_set = sorted(set(number))
print (f'The second largest digit in the number entered is {sorted_numbers_set[len(sorted_numbers_set)-2]}')