n=int(input("enter a number"))
tup=()
for i in range(n):
    tup+=(int(input("enter element")),)
    print(tup)
   # i=''.join(tup)
   # print(i)
count=tup.count(2)
print(count)
