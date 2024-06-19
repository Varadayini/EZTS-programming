n=int(input("enter a number: "))
l=list(map(int,input("enter").split()))
# print(l)
position=0
result=0
for i in l:
    position=position+i
    if position==0:
        result+=1
print(result)    



