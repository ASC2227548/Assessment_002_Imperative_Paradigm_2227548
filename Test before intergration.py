import random

# Define the rooms, exits, items, etc.

crew_room = {
    'name': 'Crew Room',
    'description': 'You awaken in a dimly lit room. The air is still, and you can hear distant hums of alarms.\nYou need to find your crew members. The door is towards the south, there is a cupboard to the west.',
    'exits': {'S': 'Corridor'},
    'items': {}
}

corridor = {
    'name': 'Corridor',
    'description': 'You find yourself in a long corridor. There are doors towards the West and South.',
    'exits': {'S': 'Control Room', 'W': 'Storage Room', 'N': 'Cargo Room'},
    'items': {}
}

control_room = {
    'name': 'Control Room',
    'description': 'You enter a room filled with control panels. A computer screen flickers on the west side of the room.',
    'exits': {'N': 'Corridor', 'W': 'West Control Room'},
    'items': {},
    'locked': True,
    'lock_combination': [3, 7, 1]  # lock combination
}

storage_room = {
    'name': 'Storage Room',
    'description': 'A room filled with boxes and supplies. There is a small locked door in the corner to the North, or return to the corridor to the East.',
    'exits': {'N': 'Small Door', 'E': 'Corridor', 'S': 'South Storage Room'},
    'items': {},
    'locked': True,
}

cargo_room = {
    'name': 'Cargo Room',
    'description': 'A room with crates and vehicles. There is a box to the west, or return to the corridor to the south.',
    'exits': {'S': 'Corridor',},
    'items': {'MEDKIT': 1}
}

small_door_room = {
    'name': 'Small Door',
    'description': 'A small, dimly lit room. You spot a gun on a table.',
    'exits': {'S': 'Storage Room'},
    'items': {},
    'alien': True,
    'alien_health': 50
}

west_control_room = {
    'name': 'West Control Room',
    'description': 'Nothing but a access card and a flickering screen. Return to the main control room to the east',
    'exits': {'E': 'Control Room'},
    'items': {'ACCESS CARD': 1},  # the access card
}
south_storage_room = {
    'name': 'South Storage Room',
    'description': 'You found a knife in a broken box, nothing else apart from tools and parts. Head north to return to the centre of the storage room',
    'exits': {'N': 'Storage Room'},  # Assume there's an exit back to Control Room
    'items': {'KNIFE': 1},  # Add the key to the west control room
}

# define the number pad puzzle
def solve_number_puzzle(current_room):
    print("You encounter a locked door with a numeric keypad.")

    # get the player's input for the three numbers
    guess = []
    while True:
        try:
            number = int(input("Enter the 1st number: "))
            guess.append(number)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


    while True:
        try:
            number = int(input("Enter the 2nd number: "))
            guess.append(number)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


    while True:
        try:
            number = int(input("Enter the 3rd number: "))
            guess.append(number)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # check if the guess matches the password
    if guess == current_room.get('lock_combination', []):
        print("Congratulations! The door unlocks.")
        current_room['locked'] = False
        return True
    else:
        print("Incorrect combination. The door remains locked.")
        return False


# define navigation and how its done
def navigate_room(current_room, direction):
    if direction in current_room['exits']:
        next_room_name = current_room['exits'][direction]
        next_room = rooms[next_room_name]

        # see if the room is locked
        is_locked = next_room.get('locked', False)

        if is_locked:
            # check if player has the access card
            if next_room_name == 'Control Room':
                print("The door to the Control Room is locked.")
                if solve_number_puzzle(next_room):
                    print("You unlock the door.")
                    next_room['locked'] = False
                    return next_room
                else:
                    print("The door remains locked.")
                    return current_room
            elif "ACCESS CARD" in items and items["ACCESS CARD"] > 0:
                print(f"You unlock the door with your access card and enter the {next_room_name}")
                # unlock the room
                next_room['locked'] = False
                return next_room
            else:
                print(f"The door to {next_room_name} is locked. You need an access card to enter.")
                return current_room
        else:
            # room navigation
            room_items = next_room.get('items', {})
            if room_items and room_items.keys():
                print(f"You enter the {next_room_name} and find the following items:")
                for item, quantity in room_items.items():
                    print(f"{item}: Quantity: {quantity}")

                pickup_choice = input("Do you want to pick up all items? (yes/no): ").lower()

                if pickup_choice == 'yes':
                    # pick up all items in the room
                    for item, quantity in room_items.items():
                        if item in items:
                            items[item] += quantity
                        else:
                            items[item] = quantity
                    print("You picked up the items.")
                    # clear the items in the room after picking up
                    next_room['items'] = {}
                elif pickup_choice != 'no':
                    print("Invalid input. Please enter 'yes' or 'no'.")

            return next_room
    else:
        print("Invalid direction.")
        return current_room

# define the alien fight function
def encounter_enemy(current_room, player_stats):
    if 'alien' in current_room:
        alien = current_room['alien']
        alien_health = current_room.get('alien_health', 50)
        print(f"You encounter an alien!")

        #  alien fight choice
        while player_stats['Health'] > 0 and alien_health > 0:
            print("Choose how to attack:")
            print("1. Normal Attack")
            print("2. Strong Attack")
            print("3. Quick Attack")
            attack_choice = input("Enter your choice (1-3): ")

            if attack_choice == "1":
                player_damage = random.randint(10, 20)
            elif attack_choice == "2":
                player_damage = random.randint(20, 30)
            elif attack_choice == "3":
                player_damage = random.randint(5, 15)
            else:
                print("Invalid choice. Try again.")
                continue

            print(f"You attack the alien and deal {player_damage} damage.")
            alien_health -= player_damage

            if alien_health <= 0:
                print(f"You defeated the alien!")
                del current_room['alien']
                del current_room['alien_health']
                break

            # when the alien attacks it does random damage between 5 and 15
            alien_damage = random.randint(5, 15)
            print(f"The alien attacks you and deals {alien_damage} damage.")
            player_stats['Health'] -= alien_damage

            # suit damage to give the players a sense of armour
            suit_damage = random.randint(5, 10)
            print(f"Your suit sustains {suit_damage} damage.")
            player_stats['Suit'] -= suit_damage

            print(f"Your health: {player_stats['Health']}")
            print(f"Your suit: {player_stats['Suit']}")

            if player_stats['Health'] <= 0:
                print("You've been defeated!")
                exit()

# dictionary with all the rooms
rooms = {'Crew Room': crew_room, 'Corridor': corridor, 'Control Room': control_room, 'Storage Room': storage_room,
         'Cargo Room': cargo_room, 'Small Door': small_door_room, 'West Control Room': west_control_room,
         'South Storage Room': south_storage_room}

# starting room
current_room = crew_room

# starting message
print('Welcome to Astray')
print('Awakening alone on a silent space station, the whereabouts of Dr. Mercer\'s fellow crew members are unknown.')
print(
    'Dr. Mercer must navigate through the station, find his crew-mates, and discover why the station is powered down.')
print(
    'Solve puzzles to unlock areas and use tactics and items collected in boss fights to end Dr. Mercer\'s worst nightmare.')

# dictionary with stats and inventory
player_stats = {"Health": 70, "Suit": 50, "Hunger": 65}
items = {
    "SUIT REPAIR": 0,
    "ACCESS CARD": 0,
    "GUN": 0,
    "KNIFE": 0,
    "MRE": 1,
    "MEDKIT": 1
}


while True:
    encounter_enemy(current_room, player_stats)

    # print current room information
    print(f"\nYou are in {current_room['name']}")
    print(current_room['description'])

    # print menu options
    print("\n1. Display inventory")
    print("2. Use item")
    print("3. Player Stats")
    print("4. Move to another room")
    print("5. Quit")

    # input player choice
    choice = input("Enter your choice (1-5): ")

    # if statements of player choices
    if choice == "1":
        print("INVENTORY:")
        for item, quantity in items.items():
            print(f"{item}: Quantity: {quantity}")
    elif choice == "2":
        item_to_use = input("Enter the name of the item to use: ").upper()
        if item_to_use in items and items[item_to_use] > 0:
            if item_to_use == "MEDKIT":
                if player_stats["Health"] < 100:
                    health_to_restore = min(100 - player_stats["Health"], 20)
                    player_stats["Health"] += health_to_restore
                    print(f"Used a {item_to_use}. Health increased by {health_to_restore}.")
                    items[item_to_use] -= 1
                else:
                    print(f"No need to use {item_to_use}. Health is already at 100.")
            elif item_to_use == "SUIT REPAIR":
                if player_stats["Suit"] < 100:
                    suit_to_restore = min(100 - player_stats["Suit"], 15)
                    player_stats["Suit"] += suit_to_restore
                    print(f"Used a {item_to_use}. Suit repaired {suit_to_restore}%.")
                    items[item_to_use] -= 1
                else:
                    print(f"No need to use {item_to_use}. Suit is already at 100%.")
            elif item_to_use == "MRE":
                if player_stats["Hunger"] < 100:
                    hunger_to_restore = min(100 - player_stats["Hunger"], 10)
                    player_stats["Hunger"] += hunger_to_restore
                    print(f"Used a {item_to_use}. Hunger decreased by {hunger_to_restore}%.")
                    items[item_to_use] -= 1
                else:
                    print(f"No need to use {item_to_use}. Hunger is already at 100%.")
            else:
                print("Invalid item name.")
        else:
            print(f"You don't have {item_to_use} in your inventory.")
    elif choice == "3":
        print(player_stats)
    elif choice == "4":
        direction = input("Enter the direction to move (N/S/E/W): ").upper()
        current_room = navigate_room(current_room, direction)
    elif choice == "5":
        print("Exiting the game. Goodbye")
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
