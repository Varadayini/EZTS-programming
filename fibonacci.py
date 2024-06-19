n=int(input("enter the no of terms"))
a=0
b=1
if n==1:
    print(a)
else:        
    print(a)
    print(b)
    for i in range(n-2): # -2 because already a and b is defined so -2 to get the terms equal to input
        c=a+b
        print(c)
        a,b=b,c
