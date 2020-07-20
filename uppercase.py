'''5. Write a program to count the number of capital letters and display the position of each capital letter in a user
entered string via keyboard'''

string=input("Enter the string:")
lis=[]
lis1=[]
for i in range(0,len(string)):
    if(string[i].isupper()):
        lis.append(string[i])
        lis1.append(i)
print("Captital letter  :  Position")
for i in range(0,len(lis)):
    print(lis[i],"  :  ",lis1[i])

print("No of uppercase letters:",len(lis))
