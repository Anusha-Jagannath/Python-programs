'''6. Write a program to count the number of each vowel in a given string'''

s1=input("Enter the string:")
count=0
d1={"a":0,"e":0,"i":0,"o":0,"u":0,"A":0,"E":0,"I":0,"O":0,"U":0}
for i in range(0,len(s1)):
    if(s1[i]=='a' or s1[i]=='e' or s1[i]=='i' or s1[i]=='o' or s1[i]=='u' or s1[i]=='A' or s1[i]=='E' or s1[i]=='I' or s1[i]=='O' or s1[i]=='U'):
        d1[s1[i]]+=1
        count+=1

print(d1)
print("No of vowels are:",count)
