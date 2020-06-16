import math
principal = float(input("Enter credit principal: "))
annuity = float(input("Enter monthly payment: "))
interest = float(input("Enter credit interest: "))
i = interest/1200

months = math.log(annuity/(annuity-i*principal), i + 1)

years = math.floor(months/12)
remaining_months = math.ceil(months % 12)
if (years == 0 and remaining_months == 0):
    print("No time.")
elif (remaining_months == 12):
    remaining_months = 0
    years += 1    
elif(years == 0):
    print(str(remaining_months) + " months.")

if(remaining_months == 0):
    print(str(years) + " years.")
elif(years != 0 and remaining_months != 0):
    print(str(years) + " years and " + str(remaining_months) + " months.")
