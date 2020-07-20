'''The finance department of a company wants to calculate the monthly pay of one of its
employee. Monthly pay should be calculated as mentioned in the formula below and
display all the employee details. Monthly Pay= No. of hours worked in a week * Pay rate
per hour * No .of weeks in a
Month. Write a Python Program to implement the problem'''



hrs=float(input("Enter no of hours:"))
pay_rate=float(input("Enter rate of pay per hour:"))
weeks=float(input("Enter no of weeks:"))
monthly_pay=hrs*pay_rate*weeks
print("Monthly pay of an employee is:",monthly_pay)
