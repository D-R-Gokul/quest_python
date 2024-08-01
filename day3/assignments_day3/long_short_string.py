#Program to find the longest and shortest string in a list

input_words = list(input("Enter some strings separated by ' ': ").split())
print (input_words)
longest = max(input_words, key=len)
shortest = min(input_words, key=len)
print(f'The shortest string is {shortest} and longest string is {longest}')