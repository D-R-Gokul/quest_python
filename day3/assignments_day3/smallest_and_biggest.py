#Program to find the smallest and biggest number in an array of N
input_list = list(map(int,input("Enter numbers separated by ' ': ").split()))  #taking input from user
maximum = max(input_list)  #finding largest number
minimum = min(input_list)  #finding smallest number
print(f'The smallest number in array is {minimum} and largest number is {maximum}')         
2#printing first and last element of sorted array to get the smallest and largest element 