# input() access string 
prompt = "if you share your name, we can personalize the message you see"
prompt += "\n What is your first name "
name = input(prompt)
print(f"\nHello, {name}!")

# int() access Numerical Input
prompt = "how old are you ?"
age = input(prompt)
if int(age) >= 18:
    print("sth")

# while loop
prompt = "\nTell me something I will repeat back to you"
prompt += "\nEnter 'quit' to end the program"
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# flag quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active: 
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)

# break quit : while true
prompt = "\nPlease enter the name of city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True: 
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f" I'd love to go to {city.title()}!")
# make sure at least one part of program can make while-loop conditon False 
        
 # filling dict with input         
responses = {}
polling_active = True
while polling_active:
    name = input("\nwhat is your name ? ")
    response = input ("which mountain would you like to climb someday ? ")
    responses[name] = response
    repeat = input("would you like to let another person respond ? (yes / no) ")
    if repeat == 'no':
        polling_active = False
print("\n -- Poll Result -- ")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


# Function with while loop:
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q'  at any time to quit")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name} ! ")
    


