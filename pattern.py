a=int(input("enter no "))
for i in range(a): #rows
    for j in range(i+1): #columns  i+1 because 1  is excluded 0 included so only one star
        print('*',end="") # default next line it goes by using end

    print("")    # after one star in first line it goes to next line