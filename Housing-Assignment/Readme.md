
# **Problem Set 1**

This problem set will introduce you to using control flow in Python and formulating a computational 
solution to a problem. It will also give you a chance to explore bisection search. This problem set has 
three problems. 

You should save your code for the first problem as ps1a.ipynb and 
the second problem as ps1b.ipynb.
Don’t forget to include comments in your code!

Collaboration,
You may work with other students; however, each student should write up and hand in his or her
assignment separately. Be sure to indicate with whom you have worked in a comment at the start of
each file. 


## **Part A: House Hunting**
You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and
decide that you want to start saving to buy a house. As housing prices are very high in the Bay Area,
you realize you are going to have to save for several years before you can afford to make the down 
payment on a house. In Part A, we are going to determine how long it will take you to save enough
money to make the down payment given the following assumptions:
1. Call the cost of your dream home total_cost.
2. Call the portion of the cost needed for a down payment portion_down_payment. For 
simplicity, assume that 
 > portion_down_payment = 0.25 (25%).
3. Call the amount that you have saved thus far current_savings. You start with a current 
savings of $0.
4. Assume that you invest your current savings wisely, with an annual return of r
(in other words, at the end of each month, you receive an additional 
> current_savings*r/12

funds to put intoyour savings – the 12 is because r is an annual rate). Assume that your investm
ents earn a return of
> r = 0.04 (4%).
5. Assume your annual salary is annual_salary.
2
6.Assume you are going to dedicate a certain amount of your salary each month to saving for 
the down payment. Call that portion_saved. This variable should be in decimal form (i.e. 0.1 
for 10%).
7. At the end of each month, your savings will be increased by the return on your investment, 
plus a percentage of your monthly salary (annual salary / 12).
Write a program to calculate how many months it will take you to save up enough money for a down
payment. You will want your main variables to be floats, so you should cast user inputs to floats. Your 
program should ask the user to enter the following variables:
1. The starting annual salary (annual_salary)
2. The portion of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
Hints
To help you get started, here is a rough outline of the stages you should probably follow in writing your
code:

● Retrieve user input. Look at input() if you need help with getting user input. For this problem 
set, you can assume that users will enter valid input (e.g. they won’t enter a string when you 
expect an int) 

● Initialize some state variables. You should decide what information you need. Be careful about
values that represent annual amounts and those that represent monthly amounts.

Try different inputs and see how long it takes to save for a down payment. Please make your 
program print results in the format shown in the test cases below.

**Test Case 1** 
>>>
>Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of your dream home: 1 000000
Number of months: 183 
>>>
**Test Case 2** 
>>>
>Enter your annual salary: 80000 
3
Enter the percent of your salary to save, as a decimal: .15 Enter 
the cost of your dream home: 5 00000
Number of months: 105
>>>

# **Part B: Saving, with a raise**
Background 
In Part A, we unrealistically assumed that your salary didn’t change. But you are an MIT graduate, and
clearly you are going to be worth more to your company over time! So we are going to build on your
solution to Part A by factoring in a raise every six months. 
In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery). Modify 
your program to include the following.
1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage) 
2. After the 6th month, increase your salary by that percentage. Do the same after the 12th
month, the 18 months, and so on.
Write a program to calculate how many months it will take you save up enough money for a down 
payment. LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the 
required down payment percentage is 0.25 (or 25%). Have the user enter the following variables: 
1. The starting annual salary (annual_salary)
2. The percentage of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
4. The semi-annual salary raise (semi_annual_raise)
Hints
To help you get started, here is a rough outline of the stages you should probably follow in writing your
code:
● Retrieve user input.
● Initialize some state variables. You should decide what information you need. Be sure to be 
careful about values that represent annual amounts and those that represent monthly amounts. 
4
● Be careful about when you increase your salary – this should only happen after the 6th, 12th
, 18th month, and so on.
Try different inputs and see how quickly or slowly you can save enough for a down payment. Please 
make your program print results in the format shown in the test cases below. 
## **Test Case 1**
>>> 
>Enter your starting annual salary: 120000
Enter the percent of your salary to save, as a decimal: .05
Enter the cost of your dream home: 500000
Enter the semi-annual raise, as a decimal: . 03
Number of months: 142 
>>>
## **Test Case 2**
>>> 
>Enter your starting annual salary: 80000
Enter the percent of your salary to save, as a decimal: .1
Enter the cost of your dream home: 800000
Enter the semi-annual raise, as a decimal: . 03
Number of months: 159 
>>>
## **Test Case 3**
>>> 
>Enter your starting annual salary: 75000
Enter the percent of your salary to save, as a decimal: .05
Enter the cost of your dream home: 1500000
Enter the semi-annual raise, as a decimal: . 05
Number of months: 261 
>>>
