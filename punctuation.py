'''7. Write a program to remove all punctuations like “’!()-[]{};:’’’,\,<>,/,?,@,#,$,%^&*_~” from the string provided
by the user.
'''
p="“’!()-[]{};:’’’,\,<>,/,?,@,#,$,%^&*_~”"
res=""
string=input("Enter the string")
for i in range(0,len(string)):
    if string[i] not in p:
        res+=string[i]
print(res)
        
