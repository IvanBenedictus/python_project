import random
import string
from words import words

def valid_word(words):
    word = random.choice(words)
    while "-" in words or " " in words:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letter = set() # what the user has guessed

    lives = 6

    # create a cheat code
    cheat = input(f"Do you want to activate the cheat (Y/N): ").lower()
    print("")
    if cheat == "y":
        print(f"Your word is {word}. Don't cheat next time you stinky bastard!")
        print("")

    elif cheat == "n":
        print("Looking though huh? Let's see what you got!")
        print("")

    else:
        print("Inavalid input! Just play the game already!")
        print("")

    while len(word_letters) > 0 and lives > 0:
        # letter used
        # " ".join(["a", "b", "cd"]) --> "a b cd"
        print("You have used this letter: ", " ".join(used_letter))

        # what the current word is
        word_list = [letter if letter in used_letter else "-" for letter in word]
        print("Your word is: ", " ".join(word_list))

        # getting user input
        user_letter = input("Type a letter: ").upper()
        print("")
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print(f"Unlucky! You have {lives} lives left!")
                print("")
        
        elif user_letter in used_letter:
            print("You have already used that character you moron!")
            print("")

        else:
            print("Are you stupid? You can't use those character!")
            print("")

    # get here when len(word_letter) == 0 or lives == 0
    if lives == 0:
        print(f"You've failed your task! Humanity will extinct and computers will dominate the world. Your word was: {word}")
        print("")

    else:
        print(f"You lucky bastard! You've guess the word '{word}'")
        print("")

hangman()