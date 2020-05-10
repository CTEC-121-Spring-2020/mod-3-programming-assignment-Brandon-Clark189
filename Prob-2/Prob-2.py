# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Brandon Norton
'''
Your IPO comment goes here
'''

def main():
    # inputs
    print("Please input your name.")
    Name = input()
    print("Please input your hourly wage.")
    Wage = int(input())
    print("Please input the hours you work weekly.")
    Hours = int(input())
    print()
    # Wages and Overtime Bonuses
    if Hours <= 40:
        Normalwage = Hours*Wage
        Bonus = 0
        baseWage = Bonus + Normalwage
    if Hours > 40:
        Bonus = (Hours - 40) *(1.5*Wage)
        Normalwage = 40*Wage
        baseWage = Bonus + Normalwage

    

    # Taxes and Insurance
    tax = (.2*(Normalwage+Bonus))
    insurance = (.1*(Normalwage+Bonus))
    totalWage = baseWage - tax - insurance

    # Totals
    print("_______________________________________")
    print("Thank you for working today: ", Name)
    print()
    print("Your wages are: ", Normalwage)
    print()
    print("Your overtime Bonus is: ", Bonus)
    print()
    print("Total wages earned before tax are:", baseWage)
    print()
    print("Tax: ", tax)
    print()
    print("Health insurance: ", insurance)
    print()
    print("Your check for today will be: ", totalWage)
    print("_______________________________________")

main()