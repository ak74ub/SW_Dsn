#Alexander Korsunsky
#Jimson Whiskeyman
#20230123
#Lab 01 Icebreaker


#Take input 
Days = input("Please enter the total number of days of the infection : ")
print(type(Days))

Days = int(Days)
print(type(Days))


#Initial Variables
Infected = 7
Total_Infected = 0

#Rate of Infection
Rate_of_Infection = 1.2
x = 0

for x in range(0, Days):
    if(Infected<39740):
        Previous_Infected = Infected
        Infected = Infected*Rate_of_Infection
        print("The total infected on days ", x, "are : ", Infected)

print("The total infected are ", Previous_Infected)


