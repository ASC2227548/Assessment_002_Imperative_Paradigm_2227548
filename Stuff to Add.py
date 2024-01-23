#Password stuff

guess_count = 0
max_attempts = 5
correct_password = "Pass"

while guess_count < max_attempts:
    guess = input("Guess the password: ").lower()

    if guess == correct_password.lower():
        print("Correct")
        break
    else:
        guess_count += 1
        print("Incorrect")

if guess_count == max_attempts:
    print("YOU HAVE BEEN LOCKED OUT")


#