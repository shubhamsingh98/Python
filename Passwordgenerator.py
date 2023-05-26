import random

NumOfChar=int(input("Enter number of character in passord(a,1,@,etc):"))
NumOfSpChar=int(input("Enter number of SpChar in passord(@,#,etc):"))
NumOfLwCL=int(input("Enter number of LwCL in passord(a,b,etc):"))
NumOfInteger=int(input("Enter number of Integer in passord(1,2,etc):"))
NumOfUpCL=int(input("Enter number of UpCL in passord(A,B,etc):"))

AvailableSpChar=['@','#','$','%']
AvailableLwCL=['a','b','c','d','e','f']
AvailableInteger=['1','2','3']
AvailableUpCL=['A','B','C','D']

Password=[]

for i in range(NumOfSpChar):
    Password.append(random.choice(AvailableSpChar))
print(Password)
for i in range(NumOfInteger):
    Password.append(random.choice(AvailableInteger))
print(Password)
for i in range(NumOfLwCL):
    Password.append(random.choice(AvailableLwCL))
print(Password)
for i in range(NumOfUpCL):
    Password.append(random.choice(AvailableUpCL))

random.shuffle(Password)


# for i in range(NumOfSpChar):
#     ele=random.choice(AvailableSpChar).split(",")
#     Password.append(ele)
# print(Password)
# for i in range(NumOfInteger):
#     ele=random.choice(AvailableInteger).split(",")
#     Password.append(ele)
# print(Password)
# for i in range(NumOfLwCL):
#     ele=random.choice(AvailableLwCL).split(",")
#     Password.append(ele)
# print(Password)
# for i in range(NumOfUpCL):
#     ele=random.choice(AvailableUpCL).split(",")
#     Password.append(ele)
# for i in range(NumOfChar):8
#     print(Password[i],'')

#print(*Password, sep='')
for i in range(NumOfChar):
    print(''.join(Password[i]))

print(''.join(str(i) for i in Password))

# for i in range(NumOfChar):  
#     print(Password[i], end = "")  


# print(Password[i])
# print (' '.join(Password))


my_string = ''
for item in Password:
    my_string += str(item)
print(my_string)