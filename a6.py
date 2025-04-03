def Prime_Num(n):
    flag = False
    if n <=1:
        print("Not a Prime Number")
    elif(n>1):
        for i in range(2,n):
            if n%i==0:
                flag = True
                break
    if(flag == True):
        print("Not a Prime")
    else:
        print("prime")

n = int(input("Enter a number"))
Prime_Num(n)