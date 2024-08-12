class Person:
    def __init__(self, age, gender, residance):
        self.age = age
        self.gender = gender
        self.residance = residance
    def gender_discount(self):
        if(self.gender == 'm' and self.age<60):
            print("You have won a fastrack coupon worth Rs 100 ")
        if(self.gender == 'f' and self.age < 45):
            print("You have won a Nyka coupon worth of Rs 100")
            
    def is_senior(self):
        if(self.age >= 60 and self.gender == 'm') or (self.age >= 45 and self.gender == 'f'):
            print("Senior discount coupon of 15 percent applied")
            
    def is_hosteler(self):
        if(self.residance == 'h'):
            print("Discount on Groceries applied")
        
        
class Student(Person):
    def __init__(self, age, gender, residance,col_pin):
        super().__init__(age, gender, residance)
        self.colg_pin = col_pin
        print("You have a coupon on books worth Rs 500")
        self.is_senior()
        self.gender_discount()
        self.is_hosteler()
        
class Worker(Person):
    def __init__(self, age, gender, residance,off_pin):
        super().__init__(age, gender, residance)
        self.office_pin = off_pin
        self.is_senior()
        self.gender_discount()
        self.is_hosteler()
        
        
        
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
    
if(occupation_key == 1):
    colgpin = int(input("Enter college pin: "))
    student_obj = Student(age, gender_dict.get(gender_key),residance_dict.get(residance_key),colgpin)

if(occupation_key == 2):
    pin = int(input("Enter the pin of office: "))
    employee = Worker(age, gender_dict.get(gender_key),residance_dict.get(residance_key),pin)