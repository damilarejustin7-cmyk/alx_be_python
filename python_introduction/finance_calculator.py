monthly_income = int(input("Enter your monthly income:"))
monthly_expenses =  int(input("Enter your total expenses: "))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) # Assuming a 5% interest rate over one year
print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(projected_savings))