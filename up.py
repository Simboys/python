f1=open("t1.txt","r")
f2=open("r.txt","w")
for line in f1:
    for ch in line:
        if ch.islower():
            ch=chr(ord(ch)-32)
            print(ch)
        elif ch.isupper():
            ch=chr(ord(ch)+32)
            print(ch)
        f2.write(ch)


