class stack:
    def __init__(Self):
        Self.items=[]
    def push(Self,data):
        Self.items.append(data)
    def pop(Self):
        return Self.items.pop()
    def size(Self):
        return len(Self.items)
    def top(self):
        return self.items[-1]
l=[3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
o=[0]*len(l)    
s=stack()
for i in range(len(l)-1,-1,-1):
    if s.size()!=0:
        while s.size()!=0 and s.top()<=l[i]:
            if s.top() <=l[i]:
                s.pop()
    if s.size()==0:
        o[i]=-1
    else:
        o[i]=s.top()
    s.push(l[i])    
print(o)    


