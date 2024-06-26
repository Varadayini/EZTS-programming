# finding smallest positive integer. if it is not there return zero
l=list(map(int,input().split()))
m=max(l)
for i in range(len(l)):
    if l[i]>0 :
        if l[i]<m:
            m=l[i]
if m>0:
    print(m)   
else:
    print(0)       

#leetcode problem 41
l=list(map(int,input("enter").split()))
l.sort()
res=1
for i in l:
    if res==i:
        res+=1
print(res)        



        
    
        
    
        
