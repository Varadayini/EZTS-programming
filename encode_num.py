no=input("enter a number")       # didn't use int() because num can't  iterate 
res=''
for i in no:
    res=res+str(int(i)*int(i))
print(int(res))    