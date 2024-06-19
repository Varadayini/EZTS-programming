l=list(map(int,input("enter :").split()))
dis=0
max=0
for i in l:
    dis+=i
    if abs(dis)>max:
        max=abs(dis)
print(max)