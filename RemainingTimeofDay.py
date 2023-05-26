# CurrentTime=(input("Enter Current Time in HH:MM:SS format:"))

# TotalHour='246060'

# RemainingHour=(int(TotalHour[0:2])-int(CurrentTime[0:2]))
# RemainingMinute=(int(TotalHour[2:4])-int(CurrentTime[2:4]))
# RemainingSecond=(int(TotalHour[4:6])-int(CurrentTime[4:6]))

# print(f"Remaining Hour is {RemainingHour}, Remaining Minute is {RemainingMinute}, Remaining Second is {RemainingSecond}.")

CurrentTime=(input("Enter Current Time in HH:MM:SS format:"))

TotalH='24' 
TotalM='1440'
TotalS='86400'
#tm-ch*60-cm
#ts-ch*60*60-cs
RemainingHour=(int(TotalH[0:2])-int(CurrentTime[0:2]))
RemainingMinute=(int(TotalM[0:4])-(int(CurrentTime[0:2])*60+int(CurrentTime[2:4])))
RemainingSecond=(int(TotalS[0:5])-int(CurrentTime[0:2])*60*60-int(CurrentTime[4:6]))


print(f"Remaining Hour is {RemainingHour}, Remaining Minute is {RemainingMinute}, Remaining Second is {RemainingSecond}.")
