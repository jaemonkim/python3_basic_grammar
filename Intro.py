import this 

message1, message2, message3 = "hello", "python", " crash courese"
print(message1, message2, message3)

# Strings :
name = "jamon kim"
print(name.title())
print(name.upper())
#format-staing
first_name = "jaemon"
last_name = "kim"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"hello, {full_name.title()}")
# add whitespace : \t ->add a Tab,  \n ->add anewline
print("language:\n\tPython\n\tC\n\tJavaScript") 
# stip whitespace : when inputing from user
favorite_language = " python "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
#removing prefix/suffix : browser use this methods
nostarch_url = 'https://nostarch.com' # url use '
simple_url = nostarch_url.removeprefix('https://')
print(f'{nostarch_url} \n{simple_url}')
full_file_name = "requirements.txt"
simple_file_name = full_file_name.removesuffix('.txt')
print(f"{full_file_name} \n{simple_file_name}")

# List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"my first bicycle was a {bicycles[0].title()}"
print(message)
# adding : <list>.append('str), <list>.insert(n,'str')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
motorcycles.insert(1, 'triumph')
print(motorcycles)
# removing : 
del motorcycles[1]
print(motorcycles)
motorcycles.pop() # the last element in the list
print(motorcycles)
# sort 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars)) # temporarily sort
print()
cars.sort()
print(cars)
cars.reverse()
print(cars)
print(len(cars))
# for loop with lis 
magicans = ['alice', 'david', 'carolin']
for magican in magicans:
    print(f"{magican}.title(), that was a great trick ")
    print(f"I can't wait to see your next trick {magican}.title()\n")
print("Thank you, everyone. That was a great magic show!") # doing something after for loop

# list with for loop
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
# list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"sorry, we don't have {requested_topping}.")
print(f"\nfinished making your pizza!")

# dictionary
alien_0 ={}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
# add key-value
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print(alien_0)
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment 
print (f"new position : {alien_0['x_position']}")
# remove key-value
del alien_0['points']
print(alien_0)
# multi-line dictionary
favorite_language = {
    'jen':  'python',
    'sarah': 'c',
    'edward': 'rust',
    'phili': 'python'
    }
print(f"sara's favorit language is {favorite_language['sarah']}\n")
# retrieve the key when key might not exist
point_value = alien_0.get('points')
print(point_value) # None means "no value exist"

# dictionary with for loop: 
# dict.items() = dict.keys() : dict.values()
for name, language in favorite_language.items():
    print(name.title())
print("\nabove are the name of all\n")
# dictionary with for loop adding if statement
friends = ['phili', 'sarah']
for name in favorite_language.keys():
    if name in friends:
        print(f"\n{name.title()}")
        print(f"\t I see you love {language}!\n")
# particular order : sort()
for name in sorted(favorite_language.keys()):
    print(f"{name.title()} thank you for taking the poll.")
 # removing repetitive values： set()
 # datatype set->{key1, key2,..} withtout values
print(f"\nThe following languages have been mentioned")
for language in set(favorite_language.values()):
        print(language.title())

# Embed 
# dictionary in list
aliens = []
for alien_number in range(30):
    new_alien = {'cloler': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print('...')
# list in dictionary
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }  
for name, languages in favorite_languages.items():
    if len(languages) >= 2:
        print(f"\n {name}'s favorite languages are:")
        for language in languages: 
            print(f"\t {language.title()}")
    else:
        print(f"{name}'s favorite language doesn't change")
# dict in dict
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for user_name, user_info in users.items():
    print(f"\nUsername: {user_name}")
    full_name = f"user_info{'first'} {'last'}"
    location = user_info['location']
    print(f"\tFull name: {full_name}.title()")
    print(f"\tlocation: {location.title()}")

# moving elemets with while loop
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Veryfying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following user fave been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# removing all instances
pets = ['dog', 'cat', 'goldfish', 'cat', 'rabbit']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

