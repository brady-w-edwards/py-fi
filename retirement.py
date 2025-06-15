import matplotlib.pyplot as plt

def calculate_retirement_growth(start_balance, annual_salary, annual_return, contribution, company_match, years):
    months = years * 12
    monthly_return = annual_return / 12 / 100
    balances = []
    balance = start_balance
    monthly_income = annual_salary / 12
    addition = contribution * monthly_income
    

    for month in range(months + 1):
        balances.append(balance)
        balance += addition
        balance *= (1 + monthly_return)

    return balances

def plot_growth(balances, years):
    months = list(range(len(balances)))
    plt.figure(figsize=(10, 6))
    plt.plot(months, balances, label="Account Balance Over Time")
    plt.title("Retirement Account Growth")
    plt.xlabel("Months")
    plt.ylabel("Balance ($)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
