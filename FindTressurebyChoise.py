import random

NumOfBox=int(input("Enter number of bax(integer):"))
NumOfChoice= int(input("Enter number of choice(integer):"))

NB=[]
i=0
for i in range(i,NumOfBox):
    ele=input(f"Enter {i} player name(format as B1,B2,etc):").split(",")
    NB.append(ele)
print(NB)


Winning=random.choice(NB)

#Choose=input("Enter Your choice(format as B1,B2,etc):")

j=0
for j in range(NumOfChoice):
    Choose=input("Enter Your choice(format as B1,B2,etc):")
    if Winning[0]==Choose:
        print(f"Congrats Choice {Choose} is correct. You Won.Correct is {Winning}.")
    else:
        print(f"Choice {Choose} is not correct. Try again.Correct is {Winning}.")
