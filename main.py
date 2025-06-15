from retirement import *

def main():
    print("Retirement Calculator")
    start_balance = float(input("Enter starting balance ($): "))
    annual_return = float(input("Enter expected annual return (%): "))
    annual_salary = float(input("Enter your annual salary ($): "))
    contribution = float(input("Enter contribution per paycheck (%): "))
    company_match = float(input("Enter company match (%): "))
    years = int(input("Enter number of years until retirement: "))

    balances = calculate_retirement_growth(start_balance, annual_salary, annual_return, contribution, company_match, years)
    plot_growth(balances, years)

if __name__ == "__main__":
    main()