'''4.
Given below is the list of marks scored by students. Find top three scorers for
the course and also display the average marks scored by all students. Implement
the solution using Python Programming.
Student Name Marks
John 86.5
Jack 91.2
Jill 84.5
Harry 72.1
Joe 80.5'''

marks_list={"John":86.5,"Jack":91.2,"Jill":84.5,"Harry":72.1,"Joe":80.5}
sorted_keys=sorted(marks_list,key=marks_list.get,reverse=True)
for student in sorted_keys[:3]:
    print(student," : ",marks_list[student])
sum=0
for student in marks_list:
    sum+=marks_list[student]
avg=sum/5
print("Average marks all students is:",avg)
    
