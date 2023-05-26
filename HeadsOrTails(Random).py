#heads or tails
import random

Speak=input("Enter Spin(Heads/Tails):")
option=['Heads','Tails']
randomchoice=random.choice(option)

if (Speak =='Heads') or (Speak =='Tails'):
    pass
    if randomchoice==Speak:
        print(f"Congrats its {randomchoice}.")
    elif randomchoice!=Speak:
        print(f"Resuli is diffrent {randomchoice}.")
else:
    print("Enter Valid choice")
