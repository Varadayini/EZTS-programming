ctr=[0]
def tower(n,frm,to,aux,ctr):
    #print(n,frm,to,aux,"called")
    if n==0:
        #print(n,frm,to,aux,"returned with zero")
        return 
    tower(n-1,frm,aux,to,ctr)
    print(f"move {n} from {frm} to {to}")
    ctr[0]+=1
    tower(n-1,aux,to,frm,ctr)
    #print(n,frm,to,aux,"returned after completion")
    
n=3
tower(n,'A','B','C',ctr)
print(ctr)
