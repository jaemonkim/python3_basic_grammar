# function
# parameter 形参: username, argument实参:‘jaemon’
def greet_user(username):
    """display a simple greeting"""
    print(f"hello, {username.title()}")

greet_user('jeamon')

# positional arguments
# order is matter
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('panda', 'huahua')

# keyword arguments
# specify explicit arguments when calling
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# default value
def describe_pet(pet_name, animal_type='hamster'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('doudou')


# return values 
# make some operation on parameters
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formated"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an Arguments Optional:
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formated"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Return  dictionary 
def make_album(artist_name, album_title, song_number=None):
    """return """
    album = {'artist_name': artist_name, 'album_title': album_title, 'song_number': song_number}
    if song_number:
        album['song_number'] = song_number
    else:
         album = {artist_name:album_title }
    return album

playlist_1 = make_album('zico', 'artist')
playlist_2 = make_album('gd', 'blue')
playlist_3 = make_album('HYUKOH', 'paul')
playlist_4 = make_album('blackpink', 'new', '4')

pre = f"""
        {playlist_1}, 
        {playlist_2}, 
        {playlist_3},
        {playlist_4}
        """
print(pre)

# fuction with list
# passing List
def greet_users(names):
    """simple greeting"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# modifying list through function
def print_models(unprinted_designs, completed_models):
    """ passing to another list"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """ show consequences"""
    for complete_model in completed_models:
        print(complete_model)

# if I don't want to original list has been changed --> passing a copy
# function_name(list_name[:])
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(f"\noriginal funtion was: \n{unprinted_designs}\n")


# Arbitrary Number of arguments
# default arbitrary arguments --> *args
# arbitray keyword arguments --> **kargs
def make_car(manufactuer, model, **car_info):
    """car info practice"""
    car_info['manufactuer'] = manufactuer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)


# import ... 
# module -->as -->alias
import pizza_function as pizza 
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# function --> as --> alias
from pizza_function import make_pizza as mp
# all fuction --> *
from pizza_function import *

# class
# parent class
class Car:
    
    def __init__(self, make, model, year):
        """initialize atrributes to describe a car"""
        self.make = make
        self.model  = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()              
    
    def update_odometer(self, mileage):
        """set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading  = mileage
    
    def read_odometer(self):
        """print a statement showing the car mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    
      
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
used_car = Car('subaru', 'outback', 2019)
print(used_car.get_descriptive_name())

used_car.update_odometer(23500)
used_car.read_odometer()
used_car.increment_odometer(1000)
used_car.read_odometer()

# Addtional class
class Battery:
    """A simple attemp to model a bettery for an electirc care"""
    
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-KWh battery.")
        
    def get_range(self):
        """pirnt a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_ ==65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")
        

# Inheritance
 
# class Child(Parent):
#   def __init__(self, ...):
#       super().init(...)
#        self.... =         
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def fill_gas_tank(self):
        """Electric car don't have gas tanks"""
        print("This car don't have gas tanks")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
