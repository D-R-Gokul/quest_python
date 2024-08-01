# Program to Find sum of the series:1 + n - n(2) + n(3) - ..... m terms
input_n = int(input("Enter the number of which the series has to be found:  "))
input_m = int (input("Enter the number of terms required: "))
sum_of_terms = 0  # initializing sum of terms as 0

def sum_of_series(n,m):  #defining a function to find sum of the series
    final_sum = 0        #initializing variable to store final output
    for i in range (0,m):
        term= (n **i) * ((-1) **i)  #mathematical representation of the series
        final_sum += term
    return final_sum

print(f'The sum of the series with {input_n} as n and {input_m} as m is {sum_of_series(input_n, input_m)}')

##########################################
# #Find sum of the series: 1 - n + n(2) - n(3) + ..... m terms
 
# N = int(input('Enter the value of term:'))
# M = int(input('Enter the number of terms:'))
# sum_of_terms = 0
 
# for i in range(0,M):
#     term = ( N ** i) * ((-1) ** i)
#     sum_of_terms += term
 
# print('sum of the series is '+ str(sum_of_terms))