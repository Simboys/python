def perfect(n):
    def is_perfect(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num

    result = []
    i = 1
    while len(result) < n:
        if is_perfect(i):
            result.append(i)
        i += 1
    return result
n=int(input("enter a n
