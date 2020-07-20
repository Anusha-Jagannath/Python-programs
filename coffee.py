''''Aroma' Coffee factory has started producing a new blend of coffee.
They want to know the customer feedback for this new variety that they decided to give people for a try on this coffee.
On this regard, they setup a coffee kiosk in front of INOX movie theatres intended to deliver a free cup of coffee to outgoing viewers after the movie.
The only thing people have to do is to remark their rating after the coffee in a special alphanumeric feedback device available at the kiosk.
The rating is accepted in a scale of 1-5 (Terrible - Tongueblaster).
When all people completes giving feedback, the staff enters a password to see the average rating for the coffee.

NOTE:
1. Logically, it is not possible to get an initial count of number of people who are willing to drink the coffee
2. Some people might leave after having the coffee without marking the feedback
3. Rating value is not considered other than 1-5
'''

rating=[1,2,3,4,5]
detail=['Terrible','Not bad','Tasty','Awesome','Tongue blaster']
feed=[]
count=0
skip=0
   
while(True):
    #print(count)
    print("\n1.Feedback")
    print("2.Skip feedback")
    print("3.Compute")
    print("4.Exit")
    ch=int(input("Enter the choice: "))
    if(ch==1):
        print("1-Terrible,2-Not bad,3-Tasty,4-Awesome,5-Tongue blaster")
        rate=int(input("Enter the rating from 1-5: "))
        if rate in rating:
            print("Thank you for valuable feeback")
            feed.append(rate)
            count=count+1
            #print(count)
            #print(feed)
        else:
            print("Invalid rating")
    elif(ch==2):
        print("Feedback skipped")
        skip=skip+1 #no of customer skipped coffee
        continue
    elif(ch==3):
        passw=input("Enter the password:")
        if(passw=="coffee"):
            avg=sum(feed)//count
            d=detail[avg-1]
            print("Average rating for the coffee is: ",avg)
            print("Coffee is : ",d)
            print("No of customer given the feedback: ",count)
            print("No of customer skipped the feedback: ",skip)
            print("Thank you")
        else:
            print("incorrect password")
    elif(ch==4):
        break
    else:
        print("invalid choice")
        
