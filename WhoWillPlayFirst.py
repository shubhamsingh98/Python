
import random

NumOfPlayers=int(input("Enter Number of players(Integer):"))
i=0
Name=[]
for i in range(i,NumOfPlayers):
    ele=input(f"Enter {i} player name:").split(",")
    Name.append(ele)
print(Name)

random.shuffle(Name)

j=0
for j in range (j,NumOfPlayers):
    print(f"{Name[j]} will play at {j+1} order")
