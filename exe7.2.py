import re
n=input("enter a string")
pattern="TH{2,3}"
if re.search(pattern,n):
    print("found")
else:
    print("not found")
