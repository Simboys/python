class parenth:
    s1=""
    def __init__(self):
        self.s1=""
    def __init__(self,s1):
        self.s1=s1
    def check(self,ch1,ch2):
        if ch1=="{" and ch2=="}":
            return True
        elif ch1=="[" and ch2=="]":
            return True
        elif ch1=="(" and ch2==")":
            return True
        else:
            return False
    def checkpara(self):
        stack=[]
        flag=1
        for ch in self.s1:
            if ch=="(" or ch=="{" or ch=="[":
                stack.append(ch)
            elif ch==")" or ch=="}" or ch=="]":
                ch1=stack.pop()
                if not self.check(ch1,ch):
                    flag=0
                    break
        if flag==1:
            print("balanced")
        else:
            print("not balanced")
s=input("enter a string:")
ob=parenth(s)
print(ob.checkpara())

