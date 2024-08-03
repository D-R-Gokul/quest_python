#Direct -problem find the count of perfect squares from a list on N numbers
import math
#getting the number of customers
number_of_customers = int(input("Enter the number of customers: "))
bill_amount = []    #creating a list to store 
count_of_perfect_squares = 0
def is_perfect_square(num):
    square_root =math.ceil(math.sqrt(num))
    if(square_root**2 == num):
        return True
    else:
        return False
    
    
for i in range(number_of_customers):
    bill_amount.append(int(input(f"Enter the bill amount of customer{i+1}:")))
    
for amount in bill_amount:
    if is_perfect_square(amount):
        count_of_perfect_squares += 1
print(f"The count of perfect squares of {number_of_customers}bills  is {count_of_perfect_squares}")



# import math
# N = int(input("The no:of customers:"))
# bill_amounts = []
# count_of_perfect_squares = 0
# print(f'Enter the bill amounts of {N} customers :')
# for i in range(N):
#     amount = int(input())
#     bill_amounts.append(amount)
# print(f'Customer bill amounts are: {bill_amounts}')
# for i in range(N):
#     root = math.isqrt(bill_amounts[i])
#     if(root * root == bill_amounts[i]):
#         count_of_perfect_squares += 1
# print(f'Count of perfect squares of {N} bills is {count_of_perfect_squares}')