branch_dictionary = {1: "ECE", 2: "MECH", 3:"BCOM"}
preferance_dictionary = {1:"Maths", 2: "English", 3: "Arts"}
marketing = {'Arts', 'English'}
accounts = {"Maths"}
sales = {'Maths', 'English'}
preferance =set()


try: 
    name =  input("Please enter your name: ")
    branch_key = int(input("Enter the corresponding number: 1: ECE \n2: MECH \n3:BCOM \n"  ))

    if branch_key not in range(1,4):
        raise ValueError("Choose one from the options given ")

    preferance_key = set(map(int,input("Choose from the choices \n1: Maths \n2: English \n3:: Arts \n").split()))
    if(len(preferance_key) <1 or len(preferance_key) > 3):
        raise ValueError("Choose at least 1 not more than 3")

    marks = list(map(int,input("Enter the marks of maths english and arts separated by ' ' \n").split()))
    if(len(marks)==3):
        maths = marks[0]
        english = marks[1]
        arts = marks[2]
    else:
        raise ValueError("Enter exactly three scores")
except ValueError as e:
    print(e)
except :
    print("Something went wrong. Try again")



for i in preferance_key:
    preferance.add(preferance_dictionary.get(i))
branch = branch_dictionary.get(branch_key)


if maths > 35 and arts > 35 and english > 35:
    if branch == 'ECE':
        required_mark = arts >90 and english>90
        if marketing.issubset(preferance) and required_mark == True:
            print("You are selected for Marketting")
        else:
            print("Your preferance dont match")
    else:
        print("Your branch do not match")
        
    if branch == 'Mech':
        required_mark = maths >90 and english>90
        if sales.issubset(preferance) and required_mark == True:
            print("You are selected for Sales")
        else:
            print("Your preferance dont match")
    else:
        print("Your branch do not match")
        
    if branch == 'ECE':
        required_mark = maths>95
        if marketing.issubset(preferance) and required_mark == True:
            print("You are selected for Accounts")
        else:
            print("Your preferance dont match")
    else:
        print("Your branch do not match")
        
else:
    print("Your mark do not qualify")
    