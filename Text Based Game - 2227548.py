import random

# dictionaries with dictionaries of the rooms, exits, items or aliens and locked doors

crew_room = {
    'name': 'Crew Room',
    'description': 'You awaken in a dimly lit room. The air is still, and you can hear distant hums of alarms.\nYou need to find your crew members. The door is towards the south.',
    'exits': {'S': 'Corridor'},
    'items': {}
}

cafe = {
    'name': 'Cafe',
    'description': 'You find the cafe, something catches your eye south of the room.',
    'exits': {'S': 'South Cafe', 'W': 'Corridor'},
    'items': {},


}

south_cafe = {
    'name': 'South Cafe',
    'description': 'You find some supplies. You also see a piece of paper with something you crew-member wrote, "THE 3rd OF JULY(7th MONTH) IS THE 1st TIME I WAS HAPPY". Return to the cafe to the north',
    'exits': {'N': 'Cafe'},
    'items': {'MEDKIT': 1, 'SUIT REPAIR': 1},


}
corridor = {
    'name': 'Corridor',
    'description': 'You find yourself in a long corridor. There are doors towards the North, East, West and South.',
    'exits': {'S': 'Control Room', 'W': 'Storage Room', 'N': 'Cargo Room', 'E': 'Cafe'},
    'items': {}
}

control_room = {
    'name': 'Control Room',
    'description': 'You enter a room filled with control panels. A computer screen flickers on the west side of the room. Return to the corridor to the north.',
    'exits': {'N': 'Corridor', 'W': 'West Control Room'},
    'items': {},
    'locked': True,
    # lock combination
    'lock_combination': [3, 7, 1]
}

storage_room = {
    'name': 'Storage Room',
    'description': 'A room filled with boxes and supplies. There is a small door in the corner to the North and a broken box south of the room, or return to the corridor to the East.',
    'exits': {'N': 'Small Hidden Room', 'E': 'Corridor', 'S': 'South Storage Room'},
    'items': {},
    # set the room to be locked
    'locked': True,
}

cargo_room = {
    'name': 'Cargo Room',
    'description': 'A room with crates and vehicles. There is a box to the west, a lcoked door north or return to the corridor to the south.',
    'exits': {'S': 'Corridor', 'N': 'A Dark Room'},
    'items': {},
    'locked': True,
    'lock_combination': [1, 0, 1]
}

boss_room = {
    'name': 'A Dark Room',
    'description': 'A room with red blinking lights and a massive dark figure standing in the corner. Return to the cargo room towards the south.',
    'exits': {'S': 'Cargo Room','N': 'Escape Room'},
    'items': {},
    'alien': True,
    'alien_health': 150
}

escape_room = {
    'name': 'Escape Room',
    'description': 'You unlocked the escape pod room, leave the ship!! or return to the dark room to the south.',
    'exits': {'S': 'Boss Room',},
    'items': {},

}

small_room = {
    'name': 'Small Hidden Room',
    'description': 'A small, dimly lit room. You see a unknown green liquid everywhere, You spot a crewmate with something in their hand, a math equation? "(50×2)+(25×2)−49", what could this unlock? Go south to return to the storage room.',
    'exits': {'S': 'Storage Room'},
    'items': {},
    'alien': True,
    'alien_health': 50,
    'locked': True,
    'lock_combination': [9, 7, 0 ]

}

west_control_room = {
    'name': 'West Control Room',
    'description': 'Nothing but a access card and a flickering screen. Return to the main control room to the east',
    'exits': {'E': 'Control Room'},
    # there will be one access card in the west control room
    'items': {'ACCESS CARD': 1},
}
south_storage_room = {
    'name': 'South Storage Room',
    'description': 'You found a knife in a broken box, and a code writen in blood on the wall, it reads "970". Head north to return to the centre of the storage room',
    # exit back to Control Room
    'exits': {'N': 'Storage Room'},
    # Add the key to the west control room
    'items': {'KNIFE': 1, 'SUIT REPAIR': 1},
}

# define the number pad puzzle, this can be used to multiple doors now
def number_puzzle(current_room):
    print("You encounter a locked door with a numeric keypad.")

    # get the player's input for the three numbers
    guess = []
    while True:
        # try and except block for exception handling
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
        # if the current room has the is_locked variable and the password is right it sets to false to unlock the door.
        current_room['locked'] = False
        # once the player gets it right no need to run again
        return True
    else:
        print("Incorrect combination. The door remains locked.")
        return False


# define navigation and how to navigate
def navigate_room(current_room, direction):
    # check if the input is a posible exit
    if direction in current_room['exits']:
        # get the name of the next room
        next_room_name = current_room['exits'][direction]
        # go into the rooms dict to get details
        next_room = rooms[next_room_name]

        print("Number of exit keys collected:", items['EXIT KEY'])

        # check if the next room is the escape room which needs 2 exit keys
        if next_room_name == 'Escape Room':
            if items['EXIT KEY'] == 2:
                print("You Managed to escape the ship, Congratulations!")
                exit()
            else:
                print("You need to collect 2 exit keys to escape.")

        # see if the room is locked
        is_locked = next_room.get('locked', False)

        # check if next room is locked
        if is_locked:
            # if next room is locked and one of these, then its a number puzzle
            if next_room_name == 'Control Room' or next_room_name == 'Cargo Room' or next_room_name == 'Small Hidden Room':
                print("The door to the Control Room is locked.")
                if number_puzzle(next_room):
                    print("You unlock the door.")
                    next_room['locked'] = False
                    return next_room
                else:
                    print("The door remains locked.")
                    return current_room
                # otherwise check if you can unlock door with cardz
            elif "ACCESS CARD" in items and items["ACCESS CARD"] > 0:
                print(f"You unlock the door with your access card and enter the {next_room_name}")
                next_room['locked'] = False
                return next_room
            else:
                print(f"The door to {next_room_name} is locked. You need an access card to enter.")
                return current_room

        else:
            # room navigation if no card and code needed
            # check to see what items in next room
            room_items = next_room.get('items', {})
            if room_items and room_items.keys():
                print(f"You enter the {next_room_name} and find the following items:")
                for item, quantity in room_items.items():
                    print(f"{item}: Quantity: {quantity}")

                # ask player to pick up items
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

# define the alien fight function so it can be used in different rooms aswell
def encounter_enemy(current_room, player_stats):
    # is alien in the room?
    if 'alien' in current_room:
        # get alien information
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
            # damage on alien based on random integer depending on attack type
            if attack_choice == "1":
                player_damage = random.randint(10, 20)
            elif attack_choice == "2":
                player_damage = random.randint(15, 30)
            elif attack_choice == "3":
                player_damage = random.randint(5, 15)
            else:
                print("Invalid choice. Try again.")
                # continue the loop
                continue
            # text telling player whats happening
            print(f"You attack the alien and deal {player_damage} damage.")
            alien_health -= player_damage


            # check if alien is dead
            if alien_health <= 0:
                print(f"You defeated the alien!")
                # delete alien from the room
                del current_room['alien']
                del current_room['alien_health']
                print("You are in shock but managed to kill the alien, you must save your self and get off the ship. The alien dropped a part of the escape pod key")
                # add exit key when you kill the alien
                items['EXIT KEY'] += 1
                break

            # when the alien attacks it does random damage between 5 and 20
            alien_damage = random.randint(5, 20)
            print(f"The alien attacks you and deals {alien_damage} damage.")
            player_stats['Health'] -= alien_damage

            # suit damage to give the players a sense of armour
            suit_damage = random.randint(5, 15)
            print(f"Your suit sustains {suit_damage} damage.")
            player_stats['Suit'] -= suit_damage
            # ensuring suit health doesnt go below 0. if it hits 0 then it automatically sets it to 0 so no negatives
            if player_stats['Suit'] < 0:
                player_stats['Suit'] = 0


            print(f"Your health: {player_stats['Health']}")
            print(f"Your suit: {player_stats['Suit']}")
            if player_stats['Health'] < 0:
                player_stats['Health'] = 0
                print("You've been defeated!")
                exit()


# dictionary with all the rooms
rooms = {'Crew Room': crew_room, 'Corridor': corridor, 'Control Room': control_room, 'Storage Room': storage_room,
         'Cargo Room': cargo_room, 'Small Hidden Room': small_room, 'West Control Room': west_control_room,
         'South Storage Room': south_storage_room, 'A Dark Room': boss_room, 'Cafe': cafe, 'South Cafe': south_cafe, 'Escape Room': escape_room}



# set the starting room
current_room = crew_room

# starting message
print('Welcome to Astray')
print('Awakening alone on a silent space station, the whereabouts of Dr. Mercer\'s fellow crew members are unknown.')
print(
    'Dr. Mercer must navigate through the station, find his crew-mates, and discover what the strange noises are and why the ship is powered down.')
print(
    'Solve puzzles to unlock areas, find all escape keys to flee the ship and use tactics and items collected in fights to end Dr. Mercer\'s worst nightmare.')

# dictionary with stats and inventory
player_stats = {"Health": 70, "Suit": 50}

items = {
    "SUIT REPAIR": 0,
    "ACCESS CARD": 0,
    "KNIFE": 0,
    "MEDKIT": 1,
    "EXIT KEY": 0
}


# loop to have a constant game
while True:
    # check for enemies in the current room
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
        # display inventory items
        print("INVENTORY:")
        for item, quantity in items.items():
            print(f"{item}: Quantity: {quantity}")
    elif choice == "2":
        # ask player to type which item they want to use
        item_to_use = input("Enter the name of the item to use: ").upper()
        # see if item is in inventory dict and can be used
        if item_to_use in items and items[item_to_use] > 0:
            if item_to_use == "MEDKIT":
                # check what players health is and to only restore up to 100
                if player_stats["Health"] < 100:
                    health_to_restore = min(100 - player_stats["Health"], 20)
                    player_stats["Health"] += health_to_restore
                    print(f"Used a {item_to_use}. Health increased by {health_to_restore}.")
                    items[item_to_use] -= 1
                else:
                    print(f"No need to use {item_to_use}. Health is already at 100.")
            # repair suit using same logic as health of not going over 100
            elif item_to_use == "SUIT REPAIR":
                if player_stats["Suit"] < 100:
                    suit_to_restore = min(100 - player_stats["Suit"], 15)
                    player_stats["Suit"] += suit_to_restore
                    print(f"Used a {item_to_use}. Suit repaired {suit_to_restore}%.")
                    items[item_to_use] -= 1
                else:
                    print(f"No need to use {item_to_use}. Suit is already at 100%.")

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
