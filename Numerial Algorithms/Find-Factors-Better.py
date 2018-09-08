import math

def findcators (n):

    factors = []

    while (n % 2 == 0):
        factors.append(2)
        n /= 2

    i = 3
    root = math.sqrt(n)
    print(root)

    while (i <= root):
        print("this is I", i)
        while ( n % i == 0):
            factors.append(i)
        n /= i
        i += 2

        return factors

    if (n>1):
        factors.append(n)
        return factors


num = 30
ans = findcators(num)
print(ans)