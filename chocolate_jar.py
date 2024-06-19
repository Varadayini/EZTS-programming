jar_count=int(input("enter a no"))
l=list(map(int,input("enter").split()))
A=0
for i in l:
    if i%3==0:
        A=A+i//3   # the need of // is to get a int no instead of float ex: to get 21 insted of 21.0
   # elif i%3>0:
    #     A=A+i//3+1       # can use else also instead of elif 
    else:
        A=A+i//3+1

print(A)            