#Harsha is working as programer

def filter_char(raw_string):
    filtered_string = ''
    for char in raw_string:
        if char.isalpha():
            filtered_string += char
    return filtered_string



input_string = input("Enter the unprocessed string: ")
filtered_output = filter_char(input_string)
print(f"The filtered character string is {filtered_output}")