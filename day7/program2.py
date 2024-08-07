# Name
# * Age
 
# 15% discount for all product for senior citizen
 
# * Gender
# male senior citizen (60 and above)
# female senior citizen (45 and above)

# 100 rupees nyka, fastrack, if female (<45)
# 100 coupon on titan, fastrack, if male (<60)
# ----

# *Occupation: Working, Student (PIN code should be local)
 
# College: 500 coupon on books
# Working: NA
 
# ----
# *Residence: Hosteller, Localite (Hostel name should be valid)
 
# Hosteller: Groceries
# Localite: NA
 
# ----
# * Armed Forces: Yes/No (Check from external file)
 
# Yes: Free pass for R-day parade for 2
# No: Na




name = input("Please enter your name: ")
age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female\nO. Other\nEnter any number.")
occupation = int(input("Select your occupation \n1: Student \n2: Working"))
is_hosteler = int(input("Enter \n1.hosteler \n2.non-hosteler"))
if is_hosteler == 1:
    hostel_name= input("Enter the hostel name: ")
armed_force = int(input("Enter \n1: Armed force or police member \n2: Not Armed force member"))

if age >= 60 and gender.lower() == "m":
    print("Senior citizen discount applied, thank you for shopping")
elif age >= 45 and gender.lower() == "f":
    print("Senior citizen discount applied, thank you for shopping")

elif occupation == 1 and armed_force == 1:
    print("You have won a pass for Republic day parade")
elif is_hosteler == 1 and occupation ==1:
    print("Offers on Groceries")
elif age <60 and occupation == 1  and is_hosteler == 2:
    print("500 coupon on books, Thankyou")

elif age <60 and gender.lower() == 'm':
    print("You have received Fastrack voucher worth of Rs:100 ")
elif age < 45 and gender.lower() == 'f':
    print("You have received Nyka voucher worth of Rs:100")

else:
    print("Thank you for shopping")
	