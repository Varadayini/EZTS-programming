
n=int(input("enter a no of pizzas"))
y=int(input("enter a atleast no of frnds"))
sum_digit=0
for i in range(y,n+1):
    if n%i==0:
        print(i)
        for i in str(i):
           sum_digit+=int(i)
        break                                                                         
    
print("the sum is",sum_digit)    