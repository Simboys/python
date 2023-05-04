class rsubset:
        sset=[]
        def __init__(self,sset):
            self.sset=sset
        def subset(self,sset):
            return self.generatesubset([],sorted(sset))
        def generatesubset(self,current,sset):
            if sset:
                return self.generatesubset(current,sset[1:])+self.generatesubset(current+[sset[0]],sset[1:])
            return[current]
n=int(input("enter a number"))
print("enter the set elements")
set1=[]
for i in range(0,n):
    set1.append(int(input()))
ob=rsubset(set1)
print(ob.subset(set1))
