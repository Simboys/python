class pow:
    power=0
    base=1
    def __init__(self,power,base):
        self.power=power
        self.base=base
    def resto(self):
        return (base*power)
    def __str__(self):
        return "base={}\n,power={}\n".format(self.base,self.power)
base=int(input("enter a base:"))
power=int(input("enter a power:"))
p=pow(base,power)
print(p.resto())
