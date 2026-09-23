import random
import time

def wait():
    time.sleep(0.8)

def start():
    print("\nWelcome to the Number Guessing Game!")
    wait()
    print("I am thinking of a number between 1 and 100.")
    wait()
    print("You have to guess the number")
    wait()
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Normal (5 chances)")
    print("3. Hard (3 chances)")
    choice = str(input("Select from 1-3:\n"))
    if choice == "1":
        print("\nStarting easy mode ...\n")
        attempts = 10
        wait()
    elif choice == "2":
        print("\nStarting normal mode ...\n")
        attempts = 5
        wait()
    elif choice == "3":
        print("\nStarting hard mode ...\n")
        attempts = 3
        wait()
    else:
        wait()
        print("Please choose a valid option !")
        exit()

    random_number = random.randint(1,100)
    print("I have guessed a number, try guess it !")

    tries = 0

    while attempts != 0:
        guess = input("Enter a guess !\n")

        try:
            int(guess)
        except ValueError:
            print("Enter a valid number")
            exit()

        if guess == random_number:
            attempts -= 1
            tries += 1
            win = True
            break
        elif guess < random_number:
            wait()
            attempts -= 1
            tries += 1
            print(f"Too small !")
            print(f"Attempts left {attempts}")
        elif guess > random_number:
            wait()
            attempts -= 1
            tries += 1
            print(f"Too big !")
            print(f"Attempts left {attempts}")

    if win == True:
        print(f"\nYou have successfully guessed the number in {tries} tries !\n")
    else:
        print("\nYou played well!\n Better luck next time\n")

start()