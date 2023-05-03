n=int(input("enter a number:"))
sum=0
temp=n
while n>0:
    rem=n%10
    sum+=rem*rem*rem
    n//=10
if sum==temp:
    print("armstrong")
else:
    print("not armstrong")

