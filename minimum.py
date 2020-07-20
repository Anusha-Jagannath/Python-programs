'''10. Write a function that returns the index of the smallest element in a list of integers. If the number of such
elements is greater than 1,return the smallest index. Use the following header:
def indexOfSmallestElement(lst):
Write a test program that prompts the user to enter a list of numbers, invokes this function to return the
index of the smallest element and displays the index.'''
def indexOfSmallestElement(l1):
    small=min(l1)
    return l1.index(small)

l1=[]
n=int(input("Enter no of elemnts:"))
print("Enter the elements:")
for i in range(0,n):
    l1.append(int(input()))
print(l1)
i=indexOfSmallestElement(l1)
print("Index of smallest element is:",i)

            
    
