import random

chores = ['Vaccum', 'Mop', 'Trash', 'Patio', 'Bathroom']
default_chore = 'Vaccum '
random_chore = ''

time_woke_up = input('Did you wake up on time day? yes or no?\n')
amount_of_things_to_do = int(input('How many things do you have to do today? \n'))

if time_woke_up == 'yes' and amount_of_things_to_do < 2:
    for i in range(0, 1):
        random_chore = random.choice(chores)
        if default_chore == random_chore:
            default_chore = random.choice(chores)
        else:
            default_chore += random_chore
elif time_woke_up == 'no' or amount_of_things_to_do < 2:
    for i in range(0, 1):
        random_chore = random.choice(chores)
        if default_chore == random_chore:
            continue
        else:
            default_chore += random_chore 
else: 
    # default_chore.split('')
    print('Go do what you gotta do worry about chores another day')

# default_chore.split('')
print(f"You can do two chores today which are {default_chore}")