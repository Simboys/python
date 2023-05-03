import re
n=input("enter a strin")
pattern=re.compile("[A-Za-z0-9]+")
ans=pattern.fullmatch(n)
if ans:
    print("match found")
else:
    print("not found")

