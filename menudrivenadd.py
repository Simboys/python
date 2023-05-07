def get_max(numbers):
    return max(numbers)
def get_min(numbers):
    return min(numbers)
def get_sum(numbers):
    return sum(numbers)
def get_product(numbers):
    product=1
    for num in numbers:
        product*=num
    return product
numbers=[]
while True:
    print("1.add a number in the list")
    print("2.get maximum number in the list")
    print("3.get minimum number in the list")
    print("4.get sum of number in list")
    print("5.get product of number in the list:")
    print("6.exit")
    choice=input("enter your choice")
    if choice=="1":
        num=int(input("enter the number"))
        numbers.append(num)
    elif choice=="2":
        if not numbers:
            print("list is empty")
        else:
            print("get_maximun number in the list is",get_max(numbers))
    elif choice=="3":
        if not numbers:
            print("list is empty")
        else:
            print("get minimum number in the list",get_min(numbers))
    elif choice=="4":
        if not numbers:
            print("list is empty")
        else:
            print("the sum of number is",get_sum(numbers))
    elif choice=="5":
        if not numbers:
            print("list is empty")
        else:
            print("product of list",get_product(numbers))
    elif choice=="6":
            print("existin")
            break        
    else:
        print("invalid choice")
