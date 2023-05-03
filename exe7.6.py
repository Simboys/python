import re
n=input("enter a string")
pattern=re.compile("[A-Za-z0-9]+fox|dog|horse[A-Za-z0-9]+")
if re.search(pattern,n):
    print("found")
else:
    print("not found")
