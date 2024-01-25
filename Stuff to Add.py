import time


hunger = 100


decrease_rate = 10
time_interval = 20


while True:

    if hunger <= 0:
        print("Game over! Your character has starved.")
        break

    hunger -= decrease_rate
    print(f"Hunger level: {hunger}")
    time.sleep(time_interval)
