n=input("enter a string")
ccnt=0
vcnt=0
if n==n[::-1]:
    print("palindrome")
else:
    print("not palindrome:")
    
print("count vowel and char")
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vcnt=vcnt+1
    else:
        ccnt=ccnt+1
print("no of vowels",vcnt)
print("no of character",ccnt)

