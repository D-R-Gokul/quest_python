#Find Nth term of series : 1 2 2 3 3 5  5 7 8 11 13 13

import pdb
import math
pdb.set_trace()
def nth_fibo_term( number):  #function to get N//2 +1 th fibo term
    n= number//2 + 1
    third_number = 0
    first_number  = 1
    second_number = 2  
    if n == 1:
        third_number = 1
    elif n == 2:
        third_number = 2
    else:
        count = 2
        while count <= n:
            third_number = first_number + second_number
            count += 1
            if count == n:
                return third_number
            first_number = second_number
            second_number = third_number
    return third_number


def check_if_prime(num):             #function to check if the number is prime
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def nth_prime_term(number):          #function to return N/2 th prime term 
    n = number/2
    j = 0
    if n == 1:
        j = 2
    elif n == 2:
        j = 3
    else:
        count  = 2
        j = 4 
        while count <= n:
            if check_if_prime(j):
                count += 1
            if count == n:
                break
            j += 1
    return j
    
print("Series: 1 2 2 3 3 5  5 7 8 11 13 13.....")
input_number = int(input("Enter the number of term of the series you require: "))
if( input_number % 2 != 0):
    nth_term = nth_fibo_term(input_number)
    print(f'{input_number}th term of this series is: {nth_term}')
else:
    nth_term = nth_prime_term(input_number)
    print(f'{input_number}th term of this series is: {nth_term}')



