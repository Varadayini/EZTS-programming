# given an integer array your task is to find the k continuous digits which gives you the maximim sum where k is entered by user

l=[30,10,2,3,4,40,3,5,6,3,5,9,8,9,6,10,10,10,70]

sum=max=0
k=int(input(" enter the no of continuous digit: "))
for i in range(0,len(l)-(k-1)): 
    sum=0
    for j in range(0,k):
        sum+=l[i+j]    
    if max<sum:
        max=sum
        pos=i   


print(max)
for j in range(0,k):
    print(l[pos+j])
