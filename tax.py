basic_salary=float(input("Enter the basic salary:"))
allowance=float(input("Enter the allowance:"))
grosspay=basic_salary+allowance
if(grosspay<5000):
    tax=0
elif(grosspay>5000 and grosspay<=10000):
    tax=0.1*grosspay
elif(grosspay>=1000 and grosspay<=20000):
    tax=0.2*grosspay
else:
    tax=0.3*grosspay
netpay=grosspay-tax
print("Total salary:",grosspay)
print("Income tax is:",tax)
print("Net pay is:",netpay)
