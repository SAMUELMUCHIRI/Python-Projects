'''
first we are requesting input from the user 

'''
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the portion of your salary to be saved: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual salary raise: '))

#initializing variables and constants 
months = 0
current_savings = 0
r = 0.04
# Calculate amount needed for down payment
portion_down_payment = 0.25 * total_cost
#calculate the monthly savings
monthly_salary = annual_salary / 12

while current_savings < portion_down_payment:
    current_savings += current_savings * r / 12
    current_savings += monthly_salary * portion_saved
    months += 1
    if months % 6 == 0:
        monthly_salary += semi_annual_raise * monthly_salary

print('Number of months:', months)