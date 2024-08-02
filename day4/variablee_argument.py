#understanding variable argument 
def varArgFunction1(*arguments):
    print(arguments)
    print(type(arguments)) # tuple
 
def varArgFunction2(*arguments):
    for i in range(len(arguments)):
        print(arguments[i])
        
def varArgFunction3(*arguments):
    print(arguments)
    # arguments[1] = 22 # TypeError
    arguments[5][0] = 20 # even though the list is inside the tuple, we can modify it.
    print(arguments)
    arguments[5].append(50)
    print(arguments)

varArgFunction3(1, 2, 4, 'list', 4.5, [2, 3, 5])


varArgFunction1(1, 2, 4)
varArgFunction1()
varArgFunction1('list', 'tuple', 'set', 'dictionary')

varArgFunction2(1, 2, 4)
varArgFunction2()
varArgFunction2('list', 'tuple', 'set', 'dictionary')

''''
def varArgFunction2(*arguments):
        print(arguments)

def varArgFunction2(*arguments):
    for i in range(len(arguments)): #Loop with range() function
        print(arguments[i])

def varArgFunction2(*arguments):
    for element in arguments: # for each loop. It accesses all elements of the tuple one by one
        print(arguments[i])
'''

#can we type cast tuple of argument to list?Yes  
# def varArgFunction4(*arguments):
#     print(type(arguments))
#     # arguments[1] = 22 # TypeError
#     arguments=list(arguments)
#     arguments.append(5)
#     print(arguments)
#     print(type(arguments))
# varArgFunction4(1, 2, 4)