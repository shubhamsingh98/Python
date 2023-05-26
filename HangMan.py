import random

Dig=(''' -- ''',''' --- ''',''' ---- ''')

RandomWords=['hello','heyaa','goal']
Guess=random.choice(RandomWords)
print(Guess)

LG=int(len(Guess))

print(f"Guesss the word of length {LG}")

for i in range(0,LG):
    UG=input(print("Enter Guess Word:"))
    if Guess[0,-1]==UG:
        print(UG)
    else:
        print(RandomWords[i])
