#Print the Fibo series of n terms with 1st 2 terms as 1 and 2.
number_of_lines = int(input("Enter the number of terms of fibinocci series:  "))
first =1
second=2
for i in range(number_of_lines):
    print(first)
    next_term= first + second
    first = second
    second = next_term
    