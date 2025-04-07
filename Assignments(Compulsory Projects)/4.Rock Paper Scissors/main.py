# 04 : ROCK PAPER SCISSORS
# In this Python project I working on random.choice(), if statements, and getting user 
# input. 

# rock beats scissors
# scissors beats paper
# paper beats rock

import random

def play_game():
    user_input = input("\nWhat's Your Choice? \n'R' for Rock, 'P' for Paper, 'S' for Scissors\n").lower()

    if user_input == 'r':
        user = 'rock'
        user_emoji = "✊"  
    elif user_input == 'p':
        user = 'paper'
        user_emoji = "✋"  
    elif user_input == 's':
        user = 'scissors'
        user_emoji = "✌"  
    else:
        return "Invalid Input! Please enter 'R', 'P', or 'S'."

    computer = random.choice(['rock', 'paper', 'scissors'])

    if computer == 'rock':
        computer_emoji = "✊"
    elif computer == 'paper':
        computer_emoji = "✋"
    else:
        computer_emoji = "✌"

    print(f"\nYou choose: {user_emoji} ({user})")
    print(f"Computer choose: {computer_emoji} ({computer})")

    if user == computer:
        return "It's a Tie 🤝"
    
    if is_win(user, computer):
        return "You Won! 🎉"
    return "You Lost! 💔"

def is_win(player, opponent):
    if (player == 'rock' and opponent == 'scissors') or \
        (player == 'scissors' and opponent == 'paper') or \
        (player == 'paper' and opponent == 'rock'):
        return True

print(play_game())


