class fraction:
    num=0
    den=1
    def gcd(self,a,b):
        if a==b:
            return a
        elif a>b:
            return self.gcd(a-b,b)
        else:
            return self.gcd(a,b-a)

    def __init__(self,num,den):
        g=self.gcd(num,den)
        self.num=num//g
        self.den=den//g

    def __str__(self):
        return "fraction is{}".format(self.num,self.den)
num=int(input("enter num"))
den=int(input("enter denum"))
ob=fraction(num,den)
print(ob)
