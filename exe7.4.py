import re
n=input("enter a string")
pattern=re.compile("[A-Za-z0-9]*I[A-Za-z0-9]+A$")
if pattern.match(n):
    print("found")
else:
    print("not found")
