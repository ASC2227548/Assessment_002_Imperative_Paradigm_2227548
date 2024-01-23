import random
def navigate_room(current_room, direction):
    if direction in current_room['exits']:
        return rooms[current_room['exits'][direction]]
    else:
        print("Invalid direction.")
        return current_room

# Define your rooms
starting_room = {
    'name': 'Starting Room',
    'description': 'You awaken in a dimly lit room. The air is still, and you can hear distant hums of machinery.',
    'exits': {'E': 'Corridor'},
    'items': {'FLASHLIGHT': 1}
}

corridor = {
    'name': 'Corridor',
    'description': 'You find yourself in a long corridor. There are doors to the North and West.',
    'exits': {'N': 'Control Room', 'W': 'Storage Room'},
    'items': {'MAP': 1}
}

control_room = {
    'name': 'Control Room',
    'description': 'You enter a room filled with control panels. A computer screen flickers with a message.',
    'exits': {'S': 'Corridor'},
    'items': {'ACCESS CARD': 1}
}

storage_room = {
    'name': 'Storage Room',
    'description': 'A room filled with crates and supplies. There is a door to the East.',
    'exits': {'E': 'Corridor'},
    'items': {'MEDKIT': 1}
}

# Set starting room
current_room = starting_room

# Create a dictionary to store all rooms
rooms = {'Starting Room': starting_room, 'Corridor': corridor, 'Control Room': control_room, 'Storage Room': storage_room}

print('Welcome to Astray')
print('Awakening alone on a silent space station, the whereabouts of Dr. Mercer\'s fellow crew members are unknown.')
print('Dr. Mercer must navigate through the station, find his crew-mates, and discover why the station is powered down.')
print('Solve puzzles to unlock areas and use tactics and items collected in boss fights to end Dr. Mercer\'s worst nightmare.')

player_stats = {"Health": 90, "Suit": 50, "Hunger": 75}

items = {
    "SUIT REPAIR": 1,
    "ACCESS CARD": 0,
    "GUN": 0,
    "KNIFE": 0,
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
        print("Inventory:")
        for item, quantity in items.items():
            print(f"{item}: Quantity: {quantity}")
    elif choice == "2":
        item_to_use = input("Enter the name of the item to use: ").upper()
        if item_to_use in items and items[item_to_use] > 0:
            if item_to_use == "MEDKIT":
                if player_stats["Health"] < 100:
                    player_stats["Health"] += 20
                    print(f"Used a {item_to_use}. Health increased by 20.")
                    items[item_to_use] -= 1
                else:
                    print(f"No need to use {item_to_use}. Health is already at 100.")
            elif item_to_use == "SUIT REPAIR":
                if player_stats["Suit"] < 100:
                    player_stats["Suit"] += 10
                    print(f"Used {item_to_use}. Suit Repaired by 10%.")
                    items[item_to_use] -= 1
                else:
                    print(f"No need to use {item_to_use}. Suit is already at 100%.")
            elif item_to_use == "MRE":
                if player_stats["Hunger"] < 100:
                    player_stats["Hunger"] += 15
                    print(f"Used {item_to_use}. Hunger decreased by 15%.")
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