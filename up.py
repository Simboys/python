f1=open("t1.txt")
for line in f1:
    for ch in line:
        if ch.islower():
            ch=chr(ord(ch)-32)
            print(ch)
        elif ch.isupper():
            ch=chr(ord(ch)+32)
            print(ch)


