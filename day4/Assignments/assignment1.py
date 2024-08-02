# User gives the data like this:
# kerala-tiruvanantapuram karnataka-bengaluru tamilnadu-chennai
# You have to separate the states and store in the list states[] and also the seperated capitals must be stored in capitals[]

input_string = list(input("Enter the state and capital in state-capital format: ").split())

#print(input_string)
splitted_input = []
for elements in input_string:
    splitted_input.extend(elements.split('-')) 

# print(splitted_input)
state_list = []
capital_list = []
for elements in splitted_input:
    if(splitted_input.index(elements)%2 == 0):
        state_list.append(elements)
    else:
        capital_list.append(elements)
        
print(f'State list = {state_list}')
print(f'Capital list = {capital_list}')