name = 'Cambodia'
names = ['aizwal', 'imphal', 'shillong', 'agartala']

print(name)    #prints the string name
print(name.upper())    #.upper() converts the string to upper case
print(name.count('a'))    #.count() counts the number of times the character repeating
print(name.count('A'))
print(name.upper().count('A'))  #first .upper() coverts string to upper case and .count()counts the number of times the character repeating
print(name.upper().count('a'))
print(name.find('o'))   #searches the character inside the string gives its index
print(name.find('dia'))  #search for 'dia' if yes gives index of d
print(name.find('xx'))   #search for xx if no gives -1

place = 'trivANdrum'
print(place.capitalize())  #makes the first letter of string upper case and all others lower

print(place.casefold())  #Converts string into lower case
print(place.center(20))  #Returns a centered string
print(place.encode())    #Returns an encoded version of the string
print(place.endswith('um'))    #Returns true if the string ends with the specified value
print(name.index('a'))   #similar to find() but raises value error if value is absent

print(name.isalnum())   #returns true if the string is alphanumeric

print(name.isalpha())  #returns true 

digit = "123"
print(digit.isdigit())