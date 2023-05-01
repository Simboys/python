n1=int(input("enter a first number:"))
n2=int(input("enter a second number:"))
def sumoffactor(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i;
            return sum
sum1=0
sum2=0
sum1=sumoffactor(n1)
sum2=sumoffactor(n2)
if sum1==n2+1 or sum1==n1+1:
    print("buddies")
else:
    print("not buddies")
