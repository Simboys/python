def prime(n):
    if n==1 or n==2 or n==3:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,n,2):
            if n%i==0:
                return False
        return True
n=int(input("enter a number"))
ans=prime(n)
if ans:
    print("prime")
else:
    print("not prime")
