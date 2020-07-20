n=int(input("Enter the positive interger:"))
if(n<=0):
    print("Enter the integer greater than zero:")
elif(n==1):
    f1=0
    print(f1)
elif(n==2):
    f1=0
    f2=1
    print(f1)
    print(f2)
else:
    f1=0
    f2=1
    print(f1)
    print(f2)
    if(n>2):
        for i in range(2,n):
            f3=f1+f2
            print(f3)
            f1=f2
            f2=f3
