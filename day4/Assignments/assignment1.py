# User gives the data like this:
# kerala-tiruvanantapuram karnataka-bengaluru tamilnadu-chennai
# You have to separate the states and store in the list states[] and also the seperated capitals must be stored in capitals[]

input_string = list(input("Enter the state and capital in state-capital format: ").split())
#taking input string 
splitted_input = []  #splitting string and storing 
for elements in input_string:  #taking each element of string
    splitted_input.extend(elements.split('-'))   #splitting each element by '-'

# initializing new strings
state_list = []
capital_list = []
for elements in splitted_input:  #taking each element of string
    if(splitted_input.index(elements)%2 == 0):  #checking the index position of element is odd or even
        state_list.append(elements)  #if even adding to state_list
    else:
        capital_list.append(elements)  #if odd adding to capital list
        
print(f'State list = {state_list}')
print(f'Capital list = {capital_list}')