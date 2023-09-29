# IPO DIAGRAM
#   INPUTS
#       Monthly gross income
#       Monthly paycheck deductions
#   PROCESS
#       set const for months in year
#       Request user's monthly gross income, set to variable
#       Request user's monthly paycheck deductions as an int, set to variable
#       Calculate monthly income (gross income - deductions), set to variable
#       Print monthly income. Formt ,.2f with preceeding dollar sign
#       Calculate yearly gross income (gross income * months in year), set to variable
#       Print yearly gross income. Formt ,.2f with preceeding dollar sign
#       Calculate yearly net income (yearly gross income - (deductions * months in year)), set to variable
#       Print yearly net income. Formt ,.2f with preceeding dollar sign
#   OUTPUTS
#       Monthly net income
#       Yearly gross income
#       Yearly net income


# set const for months in year
MONTHS_IN_YEAR = 12
# Request user's monthly gross income, set to variable
monthly_gross = float(input('Please input your monthly gross income: $'))
# Request user's monthly paycheck deductions as an int, set to variable
monthly_deductions= float(input('Please input your monthly deductions: $'))
# Calculate monthly income (gross income - deductions), set to variable
monthly_net = monthly_gross - monthly_deductions
# Print monthly income. Formt ,.2f with preceeding dollar sign
print(f'Monthly net income is: ${monthly_net:,.2f}')
# Calculate yearly gross income (gross income * months in year), set to variable
yearly_gross = monthly_gross * MONTHS_IN_YEAR
# Print yearly gross income. Formt ,.2f with preceeding dollar sign
print(f'Yearly gross income is: ${yearly_gross:,.2f}')
# Calculate yearly net income (yearly gross income - (deductions * months in year)), set to variable
yearly_net = yearly_gross - (monthly_deductions * MONTHS_IN_YEAR)
# Print yearly net income. Formt ,.2f with preceeding dollar sign
print(f'Yearly net income is: ${yearly_net:,.2f}')