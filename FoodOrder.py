Order=input("Enter Order(Pasta Or Momos):")
ExtraSugar=input("Do you want extra sugar(Yes/No):")
ExtraBread=input("Do you want extra bread(Yes/No):")
Pasta = 190
Momos = 180
Amount=0
ES=2
EB=5

# if (Order == 'Pasta'):
#     pass
#     if (ExtraSugar=='Yes') :
#         pass       
#         if (ExtraBread=='Yes'):
#             print(str(Amount=Pasta+ES+EB))
#         else:
#             print(str(Amount=Pasta+ES))
#     else:
#             print(str(Amount=Pasta))

# elif Order == 'Momos':
#     pass
#     if (ExtraSugar=='Yes') :
#         pass       
#         if (ExtraBread=='Yes'):
#             print(str(Amount=Momos+ES+EB))
#         else:
#             print(str(Amount=Momos+ES))
#     else:
#             print(str(Amount=Momos))
# else:
#     print("Please Enter a valid Input")

if (Order == 'Pasta'):
    Amount+=Pasta
    if (ExtraSugar=='Yes') :
        Amount+=ES       
        if (ExtraBread=='Yes'):
            Amount+=EB
elif Order == 'Momos':
    Amount+=Momos
    if (ExtraSugar=='Yes') :
        Amount+=ES       
        if (ExtraBread=='Yes'):
            Amount+=EB
else:
    print("Please Enter a valid Input")

print(Amount)
