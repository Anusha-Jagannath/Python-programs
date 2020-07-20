'''12. Suppose that a text file contains marks for 6 courses for a student in a line. Each course marks is separated by
space as delimiter. File contains marks for ‘n’ number of students in separate lines. Write a program that reads the
marks from the file for each student and displays the total and average. Your program should prompt the user to
enter a filename.'''

l=[]
i=0
file1=input("Enter the file name")
try:
    f1=open(file1,"r")
    for lines in f1:
        sum1=0
        l=lines.split()
        l.pop(0)
        for mark in range(0,len(l)):
            sum1+=mark
        avg=sum/6
        print("Marks of student",+str(i),":"+str(sum1))
        print("Average of student",+str(i),":",str(avg))
        i++
except:
    print("File not found")
        
        
        
    
