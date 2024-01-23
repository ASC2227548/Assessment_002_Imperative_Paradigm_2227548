import random
print('Welcome to Astray')
print('Awakening alone on a silent space station the whereabouts of Dr.Mercers fellow crew members is unknown.')
print('Dr.Mercer must navigate through the station and find his crewmates and find out why the station is powered down.')
print('Solve puzzles to unlock areas and use tactics and items collected in boss fights to end Dr.Mercers worst nightmare.')

player_stats = {"Health": 100, "Suit": 50, "Hunger": 75}

items = {
    "HEALTH PACK": 3,
    "SUIT REPAIR": 2,
    "MRE": 1
}

while True:
    print("\n1. Display inventory")
    print("2. Use item")
    print("3. Player Stats")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Inventory:")
        for item, quantity in items.items():
            print(f"{item}: Quantity: {quantity}")
    elif choice == "2":
        item_to_use = input("Enter the name of the item to use: ").upper()
        if item_to_use in items and items[item_to_use] > 0:
            if item_to_use == "HEALTH PACK":
                player_stats["Health"] += 20
                print(f"Used a {item_to_use}. Health increased by 20.")
            elif item_to_use == "SUIT REPAIR":
                player_stats["Suit"] += 10
                print(f"Used {item_to_use}. Suit Repaired by 10%.")
            elif item_to_use == "MRE":
                player_stats["Hunger"] += 15
                print(f"Used {item_to_use}. Hunger decreased by 15.")

            items[item_to_use] -= 1
        else:
            print(f"You don't have {item_to_use} in your inventory.")
    elif choice == "3":
        print(player_stats)
    elif choice == "4":
        print("Exiting the game. Goodbye")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")







