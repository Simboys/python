n=int(input("enter a number "))
t=()
for i in range(n):
    t+=(int(input("enter a tuple element")),)
    print(t)
b=int(input("enter a number"))
c=list(t)
if b in c:
    c.remove(b)
    print(c)
d=int(input("enter a number"))
if d in c:
    print("present")
else:
    print("not present")
pos=int(input("enter a position"))
if pos>len(c):
    print("invalid position")
else:
    print("Element from last of the given position:",c[-pos])
