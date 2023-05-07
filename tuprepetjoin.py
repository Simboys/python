'''Write a python script to accept tuple elements from user and perform following 
operations on it : 
a) Accept element from user and add it into the tuple. 
b) Convert tuple to a string. 
c) Find the repeated elements of a tuple'''

n=int(input("enter a number"))
tup=()
for i in range(0,n):
    tup+=(input("enter a tuple element"),)
    print(tup)
'''s="".join(tup)
print(s)'''
for i in tup:
    if tup.count(i)>1:
        print(i)
