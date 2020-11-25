print("How many years will you be saving?")
years = int(input("Enter numeber of years : "))

print("How much money is in your account right now?")
principal = float(input("Enter amount :"))

print("How much money do you plan on investing monthly?")
monthlyInvestment = float(input("Enter amount : "))

print("What will be the rate of interest in decimal (10% = 0.1) ?")
interest = float(input("Enter rate of interest : "))

print(' ')

monthlyInvestment = monthlyInvestment * 12
finalAmount = 0

for i in range(0, years):
    if finalAmount == 0:
        finalAmount = principal

    finalAmount = (finalAmount + monthlyInvestment) * (1 + interest)

print("Your final savings after {} will be :".format(years) + str(finalAmount))
