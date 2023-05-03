n1=int(input("enter a numebr"))
a=set()
for i in range(n1):
    ele=(int(input("enter the element")))
    a.add(ele)
    print(a)
n2=int(input("enter a number"))
b=set()
for j in range(n2):
    el=(int(input("enter the element")))
    b.add(el)
    print(b)
print(" the set differnece is given below\n")
diff1=a.difference(b)
diff2=b.difference(a)
print(diff1)
print(diff2)

print("symmetric differnece is\n")

sd=a.symmetric_difference(b)
print(sd)

print("check first check is super set of 1 set not\n")

print(a.issuperset(b))

