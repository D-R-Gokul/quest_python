#demonstration of different ways to add and delete an element in list
#ADDING ELEMENTS
# using append()
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) 

#using insert()
my_list1 = [1, 2, 3]
my_list1.insert(1, 4)  # Insert 4 at index 1
print(my_list1) 

#extend
my_list2 = [1, 2, 3]
my_list2.extend([4, 5, 6])
print(my_list2)

#using +=
my_list3 = [1, 2, 3]
my_list3 += [4, 5, 6]
print(my_list3)

#using concatnation
my_list4 = [1, 2, 3]
new_list5 = my_list4 + [4, 5, 6]
print(new_list5) 

#DELETING ELEMENTS
#remove()
my_list6 = [1, 2, 3, 4]
my_list6.remove(3)
print(my_list6)

#pop()
my_list7 = [1, 2, 3, 4]
popped_element = my_list7.pop()  # Removes the last element
print(my_list7)  # Output: [1, 2, 3]
print(popped_element) 

popped_element = my_list7.pop(1)  # Removes the element at index 1
print(my_list7)  # Output: [1, 3]
print(popped_element)  

#using 'del'
my_list8 = [1, 2, 3, 4]
del my_list8[2]  # Removes the element at index 2
print(my_list8) 

#list comprehension
my_list9 = [1, 2, 3, 4, 5, 6]
my_list9 = [x for x in my_list if x % 2 == 0]  # Keep only even numbers
print(my_list9)

#clear()
my_list10 = [1, 2, 3, 4]
my_list10.clear()
print(my_list10) 