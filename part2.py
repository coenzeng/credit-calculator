import math
principal = int(input("Enter the credit principal:\n"))
print('What do you want to calculate?\ntype "m" - for count of months,\ntype "p" - for monthly payment')
choice = input()
months = int(input("Enter count of months:\n"))

payment = math.ceil(principal/months)

lastpayment = principal - (months - 1) * payment

if choice == "m":
    print("It takes " + str(payment) + " month to repay the credit.")
elif choice == "p":
    print("Your monthly payment = " + str(payment) + " with last month payment = " + str(math.ceil(lastpayment)))
else:
    print("invalid.")
