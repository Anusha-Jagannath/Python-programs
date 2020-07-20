'''11. Write a program that will count the number of characters, words,and lines in a file. Words are separated by a
white-space character. Your program should prompt the user to enter a filename.
'''

linecount=0
wordcount=0
charcount=0
f1=input("Enter the file:")
rfile=open(f1,'r')
for lines in rfile:
    linecount+=1
    lines.split()
    for word in lines:
        charcount+=len(word)
for lines in rfile:
    w=lines.split()
    wordcount+=len(w)
print("No of words:",wordcount)
print("No of lines:",linecount)
print("No of character:",charcount)
