# Coding tasks:
# From the discussed program, do following:
# 1. Handle inputs with exception. String operation code is given below for your refernce
# 2. Take only particular number of inputs: 1 for branch, 1 or more for pref and exact three for marks
# 3. Pseudo code is given below for your reference

# Acceptance criteria:
# Figure out 10 use cases and expected results in excel.
# The program which you have made should run for 1 preference, that is, Accounts vacancy opening.


# -------------
# [ECE, Mech, BCOM]
# [Maths, English, Art]

# * Name
# * Branch: ECE  					
# * Preference: Maths, Art
# --
# * Maths: 80
# * English: 96
# * Art: 97

# pass marks is 35

# Marketing (ECE): Art>90 + Literature>90, pass in all subject (maths > 35)

# Accounts (BCOM): Maths>95, pass in all subject (English and Arts > 35)

# Sales (MECH): Maths>90 + Literature>90, pass in all subject (Art > 35)


class InputCountError(Exception):
    def __init__(self, message):
        self.message = message


branch_dictionary = {1: "ECE", 2: "MECH", 3:"BCOM"}
preferance_dictionary = {1:"Maths", 2: "English", 3: "Arts"}


try: 
    name =  input("Please enter your name: ")
    branch_key = int(input("Enter the corresponding number: 1: ECE \n2: MECH \n3:BCOM \n"  ))

    if branch_key not in range(1,4):
        raise InputCountError("Choose one from the options given ")

    preferance_key = list(map(int,input("Choose from the choices \n1: Maths \n2: English \n3:: Arts \n").split()))
    if(len(preferance_key) <1 or len(preferance_key) > 3):
        raise InputCountError("Choose at least 1 not more than 3")

    marks = list(map(int,input("Enter the marks of maths english and arts separated by ' ' \n").split()))
    if(len(marks)==3):
        maths = marks[0]
        english = marks[1]
        arts = marks[2]
    else:
        raise InputCountError("Enter exactly three scores")
except InputCountError as e:
    print(e)
except :
    print("Something went wrong. Try again")

preferance = set()
branch = branch_dictionary.get(branch_key)
for i in preferance_key:
    preferance.add(preferance_dictionary.get(i))
marketing = {'Arts', 'English'}
accounts = {"Maths"}
sales = {'Maths', 'English'}

if branch == 'ECE':
    if marketing.issubset(preferance):
        if maths > 35 and arts >90 and english >90:
            print("You are selected for Marketting")
        else:
            print("Your marks do not qualify")
    else:
        print("Your preferance do not align with the requirements")

elif branch == 'BCOM':
    if accounts.issubset(preferance):
        if maths > 90 and arts >35 and english >35:
            print("You are selected for Accounting")
        else:
            print("Your marks do not qualify")
    else:
        print("Your preferance do not align with the requirements")

else:
    if sales.issubset(preferance):
        if maths > 90 and arts >35 and english >90:
            print("You are selected for Sales")
        else:
            print("Your marks do not qualify")
    else:
        print("Your preferance do not align with the requirements")