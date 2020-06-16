import math
a = float(input("Enter monthly payment: "))
n = float(input("Enter count of periods: "))
interest = float(input("Enter credit interest: "))
i = interest/1200

credit_principle = math.floor(a/((i * pow(1+i, n))/(pow(1+i, n) - 1)))
print("Your credit principle = " + credit_principle + "!")

