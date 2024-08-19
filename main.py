def calculate_tax(income):
    # tax brackets and rates
    brackets = [
        (10000, 0.10),   # 10% for income up to $10,000
        (30000, 0.15),   # 15% for income up to $30,000
        (100000, 0.20),  # 20% for income up to $100,000
        (float('inf'), 0.25)  # 25% for income above $100,000
    ]

    tax = 0
    previous_limit = 0

    for limit, rate in brackets:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break

    return tax

# Example usage
income = float(input("Enter your income: $"))
tax_owed = calculate_tax(income)
print(f"Total tax owed: ${tax_owed:.2f}")

def calculate_tax(income, capital_gains, deductions, tax_credits):
    # Define tax brackets and rates for regular income
    income_brackets = [
        (9875, 0.10),   # 10% for income up to $9,875
        (40125, 0.12),  # 12% for income up to $40,125
        (85525, 0.22),  # 22% for income up to $85,525
        (163300, 0.24), # 24% for income up to $163,300
        (207350, 0.32), # 32% for income up to $207,350
        (518400, 0.35), # 35% for income up to $518,400
        (float('inf'), 0.37)  # 37% for income above $518,400
    ]

    # Define tax brackets and rates for capital gains
    capital_gains_brackets = [
        (40000, 0.00),  # 0% for capital gains up to $40,000
        (441450, 0.15), # 15% for capital gains up to $441,450
        (float('inf'), 0.20)  # 20% for capital gains above $441,450
    ]

    # Apply deductions to regular income
    taxable_income = max(0, income - deductions)

    # Calculate tax on regular income
    income_tax = 0
    previous_limit = 0
    for limit, rate in income_brackets:
        if taxable_income > limit:
            income_tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            income_tax += (taxable_income - previous_limit) * rate
            break

    # Calculate tax on capital gains
    capital_gains_tax = 0
    previous_limit = 0
    for limit, rate in capital_gains_brackets:
        if capital_gains > limit:
            capital_gains_tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            capital_gains_tax += (capital_gains - previous_limit) * rate
            break

    # Total tax before credits
    total_tax = income_tax + capital_gains_tax

    # Apply tax credits
    total_tax = max(0, total_tax - tax_credits)

    return total_tax

# Example usage
income = float(input("Enter your regular income: $"))
capital_gains = float(input("Enter your capital gains: $"))
deductions = float(input("Enter your deductions: $"))
tax_credits = float(input("Enter your tax credits: $"))

tax_owed = calculate_tax(income, capital_gains, deductions, tax_credits)
print(f"Total tax owed: ${tax_owed:.2f}")
