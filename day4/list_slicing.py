#list slicing in python 

numbers = [1,2,3,4,5,6,7,8,9,10,11]

print(numbers)  #prints entire list o/p [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(numbers[0])    #prints first element o/p 1
print(numbers[-1])    #gets last element
print(numbers[-2])    #gets second last element
print(numbers[:])     #complete list 
print(numbers[3:])    #from index 3 to last
print(numbers[:6])    #upto index 6
print(numbers[1:-1])    #[2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1:8:3])    #[2, 5, 8]
print(numbers[::3])    #[1, 4, 7, 10]
#index error occurs when we try to access an element from the list which does not exists
print(numbers[8:3:-2])    #[9, 7, 5]
print(numbers[::-1])    #[11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(numbers[8:1:-1])    #[9, 8, 7, 6, 5, 4, 3]
print(numbers[1:7:2])   #[2, 4, 6]

numbers = [1,2,3]
print(numbers[:1:-2])  #[3]
numbers = [1,2,3,4]
print(numbers[:1:-2])  #[4]
numbers = [1,2,3,4,5]
