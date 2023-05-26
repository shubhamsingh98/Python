import random

NumOfPlayer=int(input("Enter number of Player(integer):"))

EnterMin= int(input("Enter a min number(numeric):"))
EnterMax= int(input("Enter a max number(numeric):"))
SysNum = random.randrange(EnterMin,EnterMax)
print(SysNum)

#adding key value pair in empty dict
dict={}
dict1={}
dictclose={}
val=0
i=0
for i in range (i,NumOfPlayer):
    NameOfPlayer= input("Enter name of choice(char):")
    PlayerChoiseNum= int(input("Enter a number(1-100):"))
    dict[PlayerChoiseNum] = NameOfPlayer
    for i in dict:
        if i==SysNum:
            print(f"You Won {dict[i]}")
            break
        elif i<SysNum:
            val=SysNum-i
        else:
            val=i-SysNum
        dict1[NameOfPlayer]=val


    

print(f"{min(dict1, key=dict1.get)}")



