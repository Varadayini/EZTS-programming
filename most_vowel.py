# By using dictionary
s=input("enter :")
d={}
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        if i in d:
            d[i]+=1                                                 
        else:
            d[i]=1
max_occur=max(d.values())
for i,j in d.items():
        if j==max_occur: 
             print(i)      



# by using count()
s=input("enter:").lower()              
v='aeiou'
max=0
vowel=''
for i in v:
     if s.count(i)>max:
          max=s.count(i)
          vowel=i
print(vowel)          