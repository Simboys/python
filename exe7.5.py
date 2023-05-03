import re
ip="198.32.004.4.5.3.5.3.5.3.5.3.5.3"
x=ip.count(".")
if x>3:
    print("invalid")
else:
     string=re.sub("^[0]*"," ",ip)
     string=re.sub("\.[0]*"," ",string)
print(string)
