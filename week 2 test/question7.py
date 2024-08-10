#polymorphism

class Car:
    def __init__(self, steering, wheels) :
        self.steering = steering
        self.wheels = wheels
    def steer_type(self):
        print("Cars have a steering system")
        
        
        
class Honda(Car):
    def __init__(self, steering, wheels):
        super().__init__(steering, wheels)
        
    def steer_type(self):
        if(self.steering == 'Power'):
            print("Power steering")
        else:
            print("Normal steering")
            
            
car1 = Car('normal', 4)
car1.steer_type()

car2 = Honda('Power',4)
car2.steer_type()