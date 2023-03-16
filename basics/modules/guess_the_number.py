import random

def play_guess_the_number():
    # Get the minimum and maximum values from the user
    min_value = int(input("Please enter the minimum value: "))
    max_value = int(input("Please enter the maximum value: "))

    #generate a random number between min_value and max_value
    secret_number = random.randint(min_value, max_value)

    # Print the prompt for the user to guess the number
    print(f"I am thinking of a number between {min_value} and {max_value}. Can you guess what it is?")

    # Loop until the user guess the corret number
    while True:
        guess = int(input("Guess the number: "))
        if guess == secret_number:
            print("Congratulation! You guessed my number!")
            break
        # Check if the guess is too low
        elif guess < secret_number:
            print("Your guess is too low, Try again.")
        #Check if the guess is to high
        else:
            print("Your guess is to high. Try again.")
play_guess_the_number()
