price=list(map(float,input("enter prices").split()))
weight=list(map(float,input("enter w").split()))
max_wt=int(input("enter a maximum wt"))
profit=0
ratio_list=[]
for i in range(len(price)):
    ratio_list.append(price[i]/weight[i])
while max_wt>0:
    index=ratio_list.index(max(ratio_list))    
    max_wt-=weight[index]
    profit+=price[index]
    ratio_list.pop(index)
    price.pop(index)
    weight.pop(index)
print(profit)    



