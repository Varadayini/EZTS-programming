l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
input1=input("enter the sentences:").lower()
for i in input1:                              
                                                             
    if i in l:
        l.remove(i)
print("Missing Alphabets are:")                             
print("".join(l))