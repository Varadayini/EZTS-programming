

def count_vowel(s):
    d={'A':0,'E':0,'I':0,'O':0,'U':0}
    for i in s:
        if i=='a' or i=='A' :
            d['A']+=1
        elif i=='E'or i=='e':
            d['E']+=1    
        elif i=='I'or i=='i':
            d['I']+=1    
        elif i=='O'or i=='o':
            d['O']+=1    
        elif i=='U'or i=='u':
            d['U']+=1    
    x=max(d.values())
    result=[]
    for i,j in d.items():
        if j==x:
            result.append(i)
    print(result)
    return result
    

input1=[
    ["vara","hi hello world."],
    ["abhi","hey guys."],
    ["sanjana","welcome to python"],
    ["sri","qwertyqwerty"],
]

o_p={}
for i in input1:
    o_p[i[0]]=count_vowel(i[1])
print(o_p)    


    

