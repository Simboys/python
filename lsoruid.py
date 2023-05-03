n=int(input("enter a list1:"))
lst1=[]
n1=int(input("enter a list2:\t"))
lst2=[]
for i in range(0,n):
    ele1=int(input())
    lst1.append(ele1)

for j in range(0,n1):
    ele2=int(input())
    lst2.append(ele2)
    lst1.sort()
    lst2.sort()
print("sortin the list",lst1)
print("second list sort",lst2)
union=list(set(lst1).union(lst2))
print("the union is",union)
intersection=list(set(lst1).intersection(lst2))
print("intersection",intersection)
difference=list(set(lst1).difference(lst2))
print("differences",difference)
