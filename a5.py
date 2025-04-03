def factorial(n):
    f= 1
    for i in range(1,n+15):
        f=f*i
    return f

n = int(input("Enter a number"))
result = factorial(n)
print(result)