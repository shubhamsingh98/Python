nop=int(input("Number of people:"))
ta=int(input("Total amount:"))
Ia=(ta/nop)

#print("Amount paid by " + nop " people is" + Ia+ ".")
print(Ia)

print(f"Amount paid by {nop} people is {Ia}.")

Bill=int(input("Bill amount:"))

Ga=(ta+Bill)/nop
print(f"Gross Amount paid by {nop} people is {Ga}.")

