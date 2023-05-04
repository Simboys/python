class NegativeException(Exception):
    msg=""
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return("Exception",self.msg)
try:
    n=int(input("enter a number"))
    if (n<0):
        raise(NegativeException("you are enter negative value"))
except NegativeException as Error:
        print(Error)
else:
        print(n)
