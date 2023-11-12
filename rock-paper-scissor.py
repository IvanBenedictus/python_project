import random

def play():
    user = input("Choose to play 'R' for Rock, 'P' for Paper, or 'S' for Scissor: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("It's a Tie!")
    
    elif is_win(user, computer):
        print("You've Won!")
    
    else:
        print("You've Lost! The Computer is now your Master!")

def is_win(player, opponent):
    # return true if opponent win
    # r > s, s > p, p > r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player =="p" and opponent == "r"):
        return True
    
play()