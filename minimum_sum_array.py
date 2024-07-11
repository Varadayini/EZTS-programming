n=int(input("enter no of terms"))
l=list(map(int,input("enter").split()))
sum=0
l.sort()
print(l)
avg=(l[-1]+l[-2])/2
for i in range(n):
    if l[i]<avg:
        l[i]=0
    else:
        sum+=l[i]    
        
       
print(sum) 
print(l)      
