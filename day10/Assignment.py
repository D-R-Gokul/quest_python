import sys
class Person:
    def __init__(self, age, gender, residance):
        self.age = age
        self.gender = gender
        self.residance = residance
        
    def senior(self):
        print("Senior citizen discount of 15 percent applied")

    def is_hosteler(self):
        if (self.residance == 'h'):
            print("Discount on groceries")

    def gender_discount(self):
        if(self.gender == 'm'):
            print("You won a Fastrack coupon worth 100")
        if(self.gender == 'l'):
            print("You won a Nyka coupon worth 100")


class Student(Person):
    def __init__(self,age, gender, residance, clgpin):
        super().__init__(age, gender, residance)
        self.clgpin = clgpin
        print("You have a coupon on books worth Rs 500")

class Working(Person):
    def __init__(self,age, gender, residance, office_pin):
        super().__init__(age, gender, residance)
        self.office_pin = office_pin


gender_dict ={1:'m', 2:'f'}
residance_dict ={1:'h', 2:'l'}
try: 
    age = int(input("Enter your age: "))
    gender_key = int(input("Select your gender \n1:Male \n2:Female"))
    if gender_key not in range(1, 3):
        raise ValueError
    occupation_key = int(input("Choose from option \n1:Student \n2:Working"))
    if occupation_key not in range(1, 3):
        raise ValueError
    residance_key = int(input("Select your residence \n1:Hostel \n2:Non- hostel"))
    if residance_key not in range(1, 3):
        raise ValueError

except:
    print("Please enter valid choice, Try again")

if(age >= 60 and gender_dict.get(gender_key) == 'm') or (age >=45 and gender_dict.get(gender_key) == 'f'):
    person1 = Person(age, gender_dict.get(gender_key),residance_dict.get(residance_key))
    person1.senior()
    sys.exit("Thankyou, Come Again")


if occupation_key ==1:
    colgpin = int(input("Enter college pin: "))
    stud = Student(age, gender_dict.get(gender_key),residance_dict.get(residance_key),colgpin)
    stud.is_hosteler()
    stud.gender_discount()
    sys.exit("Thankyou, Come Again")

if occupation_key ==2:
    pin = int(input("Enter the pin of office: "))
    employee = Working(age, gender_dict.get(gender_key),residance_dict.get(residance_key),pin)
    employee.is_hosteler()
    employee.gender_discount()
    sys.exit("Thankyou, Come Again")

