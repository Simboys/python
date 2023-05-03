n=int(input("enter a number"))
a=set()
for i in range(n):
     el=(int(input("enter element")))
     a.add(el)
     print(a)
n=int(input("enter a number"))
if n in a:
    a.remove(n)
    print(n,"remove from the set")
else:
    print(n,"n not found in this set")
print(a)

