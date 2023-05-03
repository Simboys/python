class circ:
    r=0
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*r*r
    def __str__(self):
        return ' radius {}'.format(self.r)
r=int(input("enter a radius"))
c=circ(r)
print(c)
print("area of circle",c.area())
