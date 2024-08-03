#You are given a string containing A and B only
def removing_adjacent_repeat(input_string):
    count_of_removal = 0
    for i in range( len(input_string)-1):
        if(input_string[i] == input_string[i + 1]):
            del list(input_string)[i]
            count_of_removal += 1
    removed_string = str(input_string)
    print(f'The removed string is {removed_string} and number of removals are {count_of_removal}')
    
    
input_string = input('Enter the string of A and B: ')
removed_string = removing_adjacent_repeat(input_string)
    
