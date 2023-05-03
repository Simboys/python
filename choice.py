def get_sum(numbers):
    return sum(numbers)
def get_min(numbers):
    return min(numbers)
def get_max(numbers):
    return max(numbers)
def get_product(numbers):
    product=1
    for num in numbers:
    
        product=product*num
        return product
    
     
    
numbers=[]
while True:
            print("1.add a number to the list")
            print("2.sum of number")
            print("3.min numbers")
            print("4.max numbers")
            print("5.product ")
            print("6.exit")
            choice=input("enter your choice:")
            if choice=='1':
                num=int(input("enter a number"))
                numbers.append(num)
            elif choice=='2':
                if not numbers:
                    print("list is empty")
                else:
                    print("sum of numbers",get_sum(numbers))
            elif choice=='3':
                if not numbers:
                    print("list is empty")
                else:
                    print("min numbers",get_min(numbers))
            elif choice=='4':
                if not numbers:
                    print("list is empty:")
                else:
                    print("max number is",get_max(numbers))
            elif choice=='5':
                if not numbers:
                    print("list is empty:")
                else:
                    print("product of",get_product(numbers))
            elif choice=='6':
                
                    print("existing")
                    break
            else:
                    print("invalid choice")

