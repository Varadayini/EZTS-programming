def comma(limit):
    count=0
    for i in range(1,limit+1):
        formatted_no="{:,}".format(i) # format method is used to format nums and strings for readiability
        count+=formatted_no.count(",")
    return count
a=int(input("enter the limit:"))
commas=comma(a)
print(commas)    





    