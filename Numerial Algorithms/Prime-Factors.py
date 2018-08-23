def findfactors(n):

    factors = []
    i = 2
    while (i < 2):
        while (n % i ==0):

            factors.append(i)
            n = n / i

        i = i + 1

    if (n>1):

        factors.append(n)

    return factors



number = 30
ans = findfactors(number)
print(ans)