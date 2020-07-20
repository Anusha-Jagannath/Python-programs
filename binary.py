l1=[]
n=int(input("Enter no of elements:"))
for i in range(0,n):
    l1.append(int(input("Enter the elemnt:")))
l1.sort()
print(l1)
key=int(input("Enter the key:"))
l=0
h=n-1
flag=0
while(l<=h):
    m=(l+h)//2
    if(l1[m]==key):
        print("key found at position:",m)
        flag=1
        break
    elif(key<l1[m]):
        h=m-1
    else:
        l=m+1
if(flag==0):
   print("key not found")
    
            
