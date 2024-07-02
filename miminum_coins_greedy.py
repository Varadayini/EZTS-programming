l=[1,5,7]
l=sorted(l,reverse=True)
print(l)
bill=18
i=0
c=0
while bill>0:
    if bill>=l[i] and i<len(l):                      
        c+=1
        bill=bill-l[i]
    else:
        i+=1
print(c)           