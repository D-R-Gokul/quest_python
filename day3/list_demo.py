#List Comprehensions

# list1=[ x**2 for x in range(10)]
# print(list1)

squares = list(map(lambda x: x**2 , range(10)))
print (squares)

words = list(map(int,input("Enter a number").split()))
print (words)