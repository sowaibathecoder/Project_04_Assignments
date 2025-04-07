# 06 : COUNTDOWN TIMER ⏳ ⏰

# In this Python project, we will create a countdown timer using the time module and while loop.

import time

def countdown(t):
    print(f"\n⏰ Timer Started for {t} seconds!\n")
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"⏳ {timer}", end="\r")  
        time.sleep(1)
        t -= 1

    print("\n\n✅ Time's up! ⏰ Timer Completed! 🎉\n")

t = input("⏱️  Enter the time in seconds: ")

countdown(int(t))
