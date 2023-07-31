import random

def roll_dice():
    # Generate a random number between 1 and 6
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Roller!")

    while True:
        # Ask the user if they want to roll the dice
        user_input = input("Press 'Enter' to roll the dice or 'q' to quit: ")

        if user_input.lower() == 'q':
            print("Thanks for rolling the dice!")
            break

        # Roll the dice and display the result
        result = roll_dice()
        print(f"You rolled a {result}")

if __name__ == "__main__":
    main()