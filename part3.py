import math

choice = input('What do you want to calculate?\ntype "a" - for annuity monthly payment\ntype "n" - for count of months,\ntype "p" - for credit principal:\n')
if choice == "a":
    principal = float(input("Enter credit principal: "))
    n = float(input("Enter count of periods: "))
    interest = float(input("Enter credit interest: "))

    i = interest/1200

    annuity_payment = math.ceil(principal * (i * pow(1+i, n))/(pow(1+i, n) - 1))
    print("Your annuity payment = $", str(annuity_payment) + "!")

elif choice == "n":
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
elif choice == "p":
    a = float(input("Enter monthly payment: "))
    n = float(input("Enter count of periods: "))
    interest = float(input("Enter credit interest: "))
    i = interest/1200

    credit_principle = math.floor(a/((i * pow(1+i, n))/(pow(1+i, n) - 1)))
    print("Your credit principle = " + str(credit_principle) + "!")