'''
first we are requesting input from the user 

'''
annual_salary=float(input("Enter your annual salary"))
t_portion_saved=float(input('Enter the percent of your salary to save, as a decimal'))
total_cost=float(input("Enter the cost of your dream home"))
#initializing variables and constants 
rate = 0.04
current_savings=0
months=0
# Calculate amount needed for down payment

down_payment = 0.25*total_cost
#calculate the monthly savings and portion saved based on annual salary
monthly_salary=annual_salary/12
portion_saved=monthly_salary*t_portion_saved
'''
number of months are incremented till the condition is fullfillled
'''
while current_savings<down_payment:
    current_savings+=((current_savings*rate)/12)+portion_saved
    months+=1
    
print("Number of months",months)



