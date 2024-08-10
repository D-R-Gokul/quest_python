# Write a code to demonstrate use of inheritance and polymorphism using below example:
# 1. Eatable
# 1.1 Vegetarian
# 1.2 Non-Vegetarian

# properties to be used: carbs, fat, protein, isPeelable, isBoneless


class Eatable:
    def __init__(self, carbs, fat, protein) :
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        
    def protein_type(self):
        print(f'Protein in food is {self.protein}')
    
    
class Vegetarian(Eatable):
    def __init__(self, carbs, fat, protein, isPeelable):
        super().__init__(carbs, fat, protein)
        self.is_peelable = isPeelable
    def protein_type(self):
        print("Protein type is plant based")
class Non_veg(Eatable):
    def __init__(self, carbs, fat, protein, isBoneless):
        super().__init__(carbs, fat, protein)
        self.is_boneless = isBoneless
        
    def protein_type(self):
        print("Protein type is animal based")
        
food1 = Eatable('rice', 'oil', 'protein powder')
food1.protein_type
        
food2 = Vegetarian('rice', 'oil', 'milk', 'banana')
food2.protein_type

        
food3 = Non_veg('rice', 'oil', 'chicken', 'squid')
food3.protein_type