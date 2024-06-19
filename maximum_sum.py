# given an integer array your task is to find the 3 continuous digits which gives you the maximim sum

l=[2,4,3,5,6,3,5,9,8,9,6,3,4,6,20]

sum=max=0
for i in range(0,len(l)-2): # -2 coz we are considering 3 elements here l=15 (l-2)=13 last term exclude so 0,12. it take 12 13 14 terms by the action of next line
    sum=l[i]+l[i+1]+l[i+2]
    if max<sum:
        max=sum
        pos=i                            # if we didnt give pos=i  it will display the last three elements irrespective of sum
print(max,l[pos],l[pos+1],l[pos+2])