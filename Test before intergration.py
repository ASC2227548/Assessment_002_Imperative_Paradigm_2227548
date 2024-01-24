def navigate_room(current_room, direction):
    if direction in current_room['exits']:
        next_room_name = current_room['exits'][direction]
        next_room = rooms[next_room_name]

        # Check if there are items in the current room
        if 'items' in current_room:
            if current_room['items']:
                print("You found the following items:")
                for item, quantity in current_room['items'].items():
                    print(f"{item}: Quantity: {quantity}")

                while True:
                    # Ask the player if they want to pick up all items in the current room
                    pickup_choice = input("Do you want to pick up all items? (yes/no): ").lower()

                    if pickup_choice == 'yes':
                        # Automatically pick up all items in the current room
                        for item, quantity in current_room['items'].items():
                            # Add the item to the player's inventory
                            if item in items:
                                items[item] += quantity
                            else:
                                items[item] = quantity

                            print(f"You picked up {quantity} {item}(s).")

                        # Clear the items in the current room
                        current_room['items'] = {}
                        break  # Exit the loop if the player provided valid input
                    elif pickup_choice == 'no':
                        break  # Exit the loop if the player doesn't want to pick up items
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")

        return next_room
    else:
        print("Invalid direction.")
        return current_room








# Define my rooms
crew_room = {
    'name': 'Crew Room',
    'description': 'You awaken in a dimly lit room. The air is still, and you can hear distant hums of alarms.\nYou need to find your crew members. The door is towards the south, there is a cupboard to the west.',
    'exits': {'S': 'Corridor'},
    'items': {'SUIT REPAIR': 1}
}

corridor = {
    'name': 'Corridor',
    'description': 'You find yourself in a long corridor. There are doors towards the West and South.',
    'exits': {'S': 'Control Room', 'W': 'Storage Room', 'N': 'Cargo Room'},
    'items': {}
}

control_room = {
    'name': 'Control Room',
    'description': 'You enter a room filled with control panels. A computer screen flickers with a message.',
    'exits': {'N': 'Corridor'},
    'items': {'ACCESS CARD': 1}
}

storage_room = {
    'name': 'Storage Room',
    'description': 'A room filled with boxes and supplies. There is a small locked door in the corner to the North, or return to the corridor to the East.',
    'exits': {'N': 'Small Door', 'E': 'Corridor'},
    'items': {'KNIFE': 1,}
}
cargo_room = {
    'name': 'Cargo Room',
    'description': 'A room with crates and vehicles. There is a box to the west, or return to the corridor to the south.',
    'exits': {'S': 'Corridor', 'N': 'Locked Room'},
    'items': {'MEDKIT': 1}
}
# Set starting room
current_room = crew_room

# Create a dictionary to store all rooms
rooms = {'Crew Room': crew_room, 'Corridor': corridor, 'Control Room': control_room, 'Storage Room': storage_room, 'Cargo Room': cargo_room}

print('Welcome to Astray')
print('Awakening alone on a silent space station, the whereabouts of Dr. Mercer\'s fellow crew members are unknown.')
print('Dr. Mercer must navigate through the station, find his crew-mates, and discover why the station is powered down.')
print('Solve puzzles to unlock areas and use tactics and items collected in boss fights to end Dr. Mercer\'s worst nightmare.')

player_stats = {"Health": 70, "Suit": 50, "Hunger": 75}

items = {
    "SUIT REPAIR": 0,
    "ACCESS CARD": 0,
    "GUN": 0,
    "KNIFE": 0,
    "MRE": 1,
    "MEDKIT": 1
}

while True:
    print(f"\nYou are in {current_room['name']}")
    print(current_room['description'])

    print("\n1. Display inventory")
    print("2. Use item")
    print("3. Player Stats")
    print("4. Move to another room")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

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
