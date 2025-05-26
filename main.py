# made by mash
import random
import time

track = []


def game(till, num):
    count = 0
    start = time.time()
    while count != till:
        try:
            guess = int(input("\nEnter your guess: "))
            if guess < 1 or guess > 100:
                print("Pick a number between 1 and 100.")
                continue

            if guess == num:
                count += 1
                end = time.time()
                print(
                    f"Congratulations! You guessed the correct number in {count} attempts. It took you {round(end - start)} sec to guess.")
                track.append(count)
                break
            else:
                count += 1
                if guess > num:

                    print(f"Incorrect! The number is less than {guess}.")
                elif guess < num:
                    print(f"Incorrect! The number is greater than {guess}.")
                if count == 2:
                    want_hint = input("Do you want a hint? (y/n): ").lower()
                    if want_hint == 'y':
                        if num % 2 == 0:
                            print("Hint: The number is even.")
                        else:
                            print("Hint: The number is odd.")
                if count == 5:
                    want_hint = input("Do you want a hint? (y/n): ").lower()
                    if want_hint == 'y':
                        rad = random.randint(1, 15)
                        low = max(1, num - rad)
                        high = min(100, num + rad)
                        print(f"Hint: The number is between {low} and {high}")

        except ValueError as e:
            print(f"Error: {e}")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


print("\nPlease select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")
print("4. Best score")
print("5. Quit")

choice = int(input("Enter your choice: "))

while choice != 5:
    num = random.randint(1, 100)
    played = False
    if choice == 1:
        print("Great! You have selected the Easy difficulty level.\n")
        game(10, num)
        played = True
    elif choice == 2:
        print("Great! You have selected the Medium difficulty level.\n")
        game(5, num)
        played = True
    elif choice == 3:
        print("Great! You have selected the Hard difficulty level.\n")
        game(3, num)
        played = True
    elif choice == 4:
        if track:
            best_scores = sorted(track)[:3]
            print(f"Top 3 scores: {best_scores}")
            print(f"You've played {len(track)} games.")

        else:
            print("You haven't played yet!")

    if played:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print("4. Best score")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
