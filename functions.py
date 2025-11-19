
def calc_balance(income, expense):
    print(f"Total expenses are {expense}")

    balance = income - expense
    return balance


def financial_status(balance):
    if balance > 0:
        return "Your balance is great!"
    if balance == 0:
        return "You are breaking even."
    elif balance  < 0:
        return "WARNING!!! You are overspending."
