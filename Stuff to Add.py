import time


hunger = 70


decrease_rate = 10
time_interval = 1


while True:

    if hunger <= 0:
        print("Game over! Your character has starved.")
        break

    player_stats['Hunger'] -- decrease_rate
    print(f"Hunger level: {hunger}")
    time.sleep(time_interval)


def alien_encounter():
    print("You encounter a hostile alien!")

    # Player's options during combat
    print("1. Aim for the head")
    print("2. Target the arms")
    print("3. Go for the legs")
    print("4. Attempt to flee")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("You successfully hit the alien's head! It takes 20 damage.")
        return 20  # damage dealt
    elif choice == "2":
        print("You target the alien's arms, but it dodges your attack. The alien counterattacks.")
        return -10  # player takes damage
    elif choice == "3":
        print("You go for the legs, slowing down the alien. It takes 10 damage but retaliates.")
        return 10  # player deals damage, but also takes some
    elif choice == "4":
        print("You attempt to flee.")
        print("The alien catches up with you as you try to flee. You take 15 damage.")
        return -15  # player takes damage
    else:
        print("Invalid choice. The alien attacks you.")
        return -15  # player takes damage
