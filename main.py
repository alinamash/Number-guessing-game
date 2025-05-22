import random
import time

track = []

def game(till, num):
    count = 0
    while count != till:
        try:
            guess = int(input("\nEnter your guess: "))
            start = int(time.strftime("%S", time.localtime()))
            if guess < 1 or guess > 100:
                print("Pick a number between 1 and 100.")
                continue

            if guess == num:
                count += 1
                end = int(time.strftime("%S", time.localtime()))
                print(f"Congratulations! You guessed the correct number in {count} attempts. It took you {end - start} sec to guess.")
                break
            elif guess > num:
                count += 1
                print(f"Incorrect! The number is less than {guess}.")
            elif guess < num:
                count += 1
                print(f"Incorrect! The number is greater than {guess}.")

        except ValueError as e:
            print(f"Error: {e}")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


print("\nPlease select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")
print("4. Quit")

choice = int(input("Enter your choice: "))

while choice != 4:
    num = random.randint(1, 100)
    if choice == 1:
        print("Great! You have selected the Easy difficulty level.\n")
        game(10, num)
    elif choice == 2:
        print("Great! You have selected the Medium difficulty level.\n")
        game(5, num)
    elif choice == 3:
        print("Great! You have selected the Hard difficulty level.\n")
        game(3, num)

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break

    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
