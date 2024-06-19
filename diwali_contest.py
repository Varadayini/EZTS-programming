n=int(input("enter how many problems are"))
p=int(input("enter time taken to travel in minutes"))
time=240-p
res=0
                         # problem 1,2,3 like that
for i in range(1,n+1):
    if i*5<time:
        res+=1
        time=time-i*5
print(res)        
