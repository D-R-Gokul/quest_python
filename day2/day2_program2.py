#Accept the food type (veg or non-veg) from the user and then prompt her for the food item number and serve her the food.
import sys
 
veg_food_items = {
    1 : 'Mysuru Filter Coffee',
    2 : 'Yummy Idly-vada',
    3 : 'Worlds soft Mysuru Mailari Dosa',
    4 : 'Bhupal Special Poha',
    5 : 'Bengaluru tamato-peanuts Upama'
}
non_veg_food_items = {
    1 : 'Egg Pokoda',
    2 : 'Chicken Biryani',
    3 : 'Fish Fry',
    4 : 'Mutton Masala'
}
food_types = {
    1 : veg_food_items,
    2 : non_veg_food_items
}
food_items = {
    1 : '1:Coffee 2:Idly-Vada 3:Dosa 4:Poha 5:Upama',
    2 : '1:Egg Pokoda 2:Chicken Biryani 3:Fish Fry'
}
 
print('Welcome to our hotel The Taste')
user_choice = int(input('1:Veg 2:Non-Veg \t Your choice please: '))
items = food_items.get(user_choice, 'Invalid')
if items == 'Invalid':
    sys.exit('Invalid choice entered')
print(items)
food_item_number = int(input('Enter the food item number that you wish:'))
if(food_item_number <0 or food_item_number >5 or (user_choice==2 and food_item_number>3)):
    print("Invalid Input")
else:
    print('Your ' + food_types.get(user_choice).get(food_item_number) + ' is here')
 
print('Thank you, Visit again')




