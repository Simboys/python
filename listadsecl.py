n=int(input("enter how many list seperated by space"))
lst=[]
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
sum=0
for i in lst:
    sum+=i
mul=1
for i in lst:
    mul*=i
print("addtion of list",sum)
print("multiplication of list",mul)
largest=max(lst)
smallest=min(lst)
sort=sorted(lst)
seclarge=sort[-2]
print("largest number is",largest)
print("smallest number is",smallest)
print("second largest",seclarge)

