s=input("enter : ").upper()
score=0
count=0
for i in s:
    if i=='H':
        count+=1
        score+=2
        if count==3:
            break
    else:
        score+=-1                                       # ypu can also include one condition that if the input is other then h or t but this is just simple to grt
        count=0
    
print("your score is ",score)            
                                                                           