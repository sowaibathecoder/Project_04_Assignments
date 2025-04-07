# 03 : GUESS THE NUMBER (USER)

# In Guess the Number Python's Project we use random module, build functions,
# work with while loops and conditionals, and get computer guess number input.

import random  

def computer_guess(x):  
    low = 1  
    high = x  
    feedback = ""  
    attempts = 0  

    print(f"Think of a number between 1 and {x}. Computer will try to guess it!")  

    while feedback != "c":  
        if low != high:  
            guess = random.randint(low, high)  
        else:  
            guess = low   

        attempts += 1  

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()  

        if feedback == "h":  
            high = guess - 1  
        elif feedback == "l":  
            low = guess + 1  

    print(f"🎉 Computer guessed your number {guess} correctly in {attempts} attempts!")  

computer_guess(100)  
