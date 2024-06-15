input1=input("enter a string").lower()
freq={}
for i in input1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1 
max_freq=max(freq.values())   
res=len(input1)-max_freq
print("minimum no of steps required to form a magic square is :",res)       
print(freq)