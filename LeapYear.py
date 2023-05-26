#Method 1
# Year = int(input("Enter The year:"))

# if Year%4 == 0:
#     if Year%100 ==0:       
#         if Year%400 ==0:
#             print(f"{Year} is a leap year")
#         else:
#             print(f"{Year} is not a leap year") 
#     else:
#         print(f"{Year} is leap year")
            
# else:
#     print(f"{Year} is not a leap year")

#Method 2

Year = int(input("Enter The year:"))

if (Year%100 == 0) and (Year%400==0):
    print(f"{Year} is a Leap year")
elif (Year%4==0) and (Year%100 !=0):       
    print(f"{Year} is a leap year")
else:
    print(f"{Year} is not a leap year")
