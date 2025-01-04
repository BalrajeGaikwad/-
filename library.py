
"""
A library charges a fine for every book returned late. For first 5 days the fine is 50 paise per day, 
for 6-10 days fine is one rupee per day and above 10 days fine is 5 rupees per day. 
If you return the book after 30 days your membership will be cancelled. 
Write a program to accept the number of days the member is late to return the book and display the fine or the appropriate message.
"""

day=int(input("Enter days :- "))

if(day>1 and day<=5):
    panenty=0.5*day
    print("panelty is 0.5 : ", panenty)
elif( day>5 and day<10):
    panenty=1*day
    print("panelty 5 : ", panenty)
elif(day > 10):
    panenty=5*day
    print("panaelty 10 :-",panenty)
elif(day>30):
    print("cancel membership")


