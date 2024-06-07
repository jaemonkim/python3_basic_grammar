# First, importing standard library module

# Then, importing module that I wrote
 
# importing class
from car_module import Car
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# importing module
import car_module
my_mustang = car_module.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = car_module.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
# importing all class
from car_module import * 

# standard library 
# random --> randint
from random import randint
r_num = randint(1, 6)
print(r_num)
# random --> choice
from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

