import re
n=input("enter a string")
pattern=re.compile("[A-Z][a-z]+")
ans=pattern.match(n)
if ans:
    print("found")
else:
    print("not found")
