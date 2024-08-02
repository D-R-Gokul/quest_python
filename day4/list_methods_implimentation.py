numbers = [1, 2, 3, 4, 5, 6]
numbers[len(numbers): ] = [7]  
print(numbers)

#numbers[len(numbers): ] = 7   "Type error because we must assign only list (iterable) not primitive "

del numbers[1:3]  #deletes elements in index 1,2
print(numbers)

del numbers[1]  #deletes elements in index 1
print(numbers)

del numbers[:]    #deletes all elements
print(numbers)

#inserting
numbers.append(1)  #inserts element to the end of list
print(numbers)

numbers[len(numbers): ] = [2,3,4,5,6,7,8,9,10]   #inserts elements to the end of the list
print(numbers)


numbers.insert(10,1) #inserts 1 to the 10 index position
print(numbers)

numbers.insert(-1,78)  #insert also works in negative indexing (adds the new element before the last element )
print(numbers)

#######################################
numbers = [23, 7, 19, 41, 29, 3, 47]
 
print('Max number = ', max(numbers))
print('Min number = ', min(numbers))
print('Number of elements = ', len(numbers))
print('Sorted numbers = ', sorted(numbers))
print('Numbers = ', numbers)
numbers.sort()
print('Numbers = ', numbers)