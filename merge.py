'''8. Consider two strings, String1 and String2 and display the merged string as output. The merged string should be
the capital letters from both the strings in the order they appear.
Sample Input:String1:ILikeC String2:MaryLikesPython
Merged string should be ILCMLPS'''

s1=input("Enter the string1:")
s2=input("Enter the string2:")
mer=""
for i in range(0,len(s1)):
    mer+=s1[i]
for i in range(0,len(s2)):
    mer+=s2[i]

print(mer)
