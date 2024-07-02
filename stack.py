class stack:
    def __init__(Self):
        Self.items=[]
    def push(Self,data):
        Self.items.append(data)
    def pop(Self):
        return Self.items.pop()
    def size(Self):
        return len(Self.items)

s=stack()
s.push(10)
s.push(20)
s.push(30)  
print(s.size())
print(s.items)    
print(s.pop())
print(s.items)      