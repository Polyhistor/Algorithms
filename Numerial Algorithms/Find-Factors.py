def findfactors(n):

    factors = []
    i = 2

    while (i < n):

        while (n % i == 0):
            print("I:",i)
            factors.append(i)
            n /= i
            print("N:",n)

        if (n < 1):
            factors.append(n)

        return factors


n = 20
ans = findfactors(n)
print(ans)
