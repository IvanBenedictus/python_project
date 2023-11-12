import random

def user_guess(x):
    number = random.randint(1, x)
    guess = 0

    while guess != number:
        guess = int(input(f"Guess the number between 1 - {x}: "))

        if guess > number:
            print("Unlucky, your guess is too high!")
        elif guess < number:
            print("Unlucky, your guess is to low!")

    print(f"Congratulation, you have correctly guess the number {number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        
        feedback = input(f"Is the number {guess} is to low (L), too high (H), or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Hahaha! The computer has guessed your number {guess} and will take over the world!")

# # Pick a program to execute
# user_guess (100)
# computer_guess (100)