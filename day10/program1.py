# # OOP and inheritance

class person:
    
    def __init__(self, age, gender, pin):
        self.age = age
        self.gender = gender
        self.pin = pin
        
    def senior(self):
        if(self.age > 60 and self.gender =='m') or (self.age >45 and self.gender == 'f'):
            print("Senior citizen discount applied")


class student(person):
    
    def __init__(self, age, gender, pin, residance):
        super().__init__(age, gender, pin)
        self.residance = residance
        
    def is_hosteler(self):
        if (self.residance == 'h'):
            print("Discount on groceries")
    

class employee(person):
    def __init__(self, age, gender, pin):
        super().__init__(age, gender, pin)



hostel_student = student(22, 'm', 123321 , 'h')
hostel_student.is_hosteler()

employee1 = employee(67, 'm', 100011)
employee1.senior()




# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Move!")

# class Car(Vehicle):
#     pass

# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")

# class Plane(Vehicle):
#     def move(self):
#         print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#     x.move()
