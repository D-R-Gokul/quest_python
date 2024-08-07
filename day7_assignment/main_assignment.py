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




#name = input("Please enter your name: ")
age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female: \nEnter any number.")
occupation = int(input("Select your occupation \n1: Student \n2: Working"))
is_hosteler = int(input("Enter \n1.hosteler \n2.non-hosteler"))

if age >= 60 and gender.lower() == "m":
    print("Senior citizen discount 15 percent applied, thank you for shopping")
elif age >= 45 and gender.lower() == "f":
    print("Senior citizen discount 15 percent applied, thank you for shopping")
else:
    if age <60 and gender== 1:
        print("You have received Fastrack voucher worth of Rs:100 ")
    else: 
        print("You have received Nyka voucher worth of Rs:100")

if age < 45:
    if occupation == 1 and is_hosteler == 2:
        print("You have won a  Rs 500 coupon on books")
    
    elif is_hosteler == 1 and occupation ==1:
        print("Offers on Groceries and Students coupon of Rs:500 on books applied")
    elif occupation == 2  and is_hosteler == 2:
        print("discount on Groceries, Thankyou")
    else:
        print("Thank you for shopping")
