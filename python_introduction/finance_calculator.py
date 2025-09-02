#collects details of monthly income and monthly expenses
monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))

#create a variable to compute monthly savings
monthly_savings = monthly_income - monthly_expenses

#create a variable for projected savings
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}")
print(f'Projected savings after one year, with interest, is: ${projected_savings}')
