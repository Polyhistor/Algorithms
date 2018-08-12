def fib(arr):

    a = 0
    b = 1
    sum = []
    even = []
    n = len(arr)

    while (b < n):

        a,b = b,a+b
        sum.append(b)

        if(b % 2 == 0):

            even.append(b)

    print(even)
    return sum






arr = list(range(10))
ans = fib(arr)
print(ans)
