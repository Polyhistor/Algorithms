import math

def findprimes(max):

    is_composite = [False] * (max + 1)

    print(is_composite)

    for i in range(4, max, 2):
        is_composite[i] = True

    print(is_composite)

    next_prime = 3
    stop_at = math.sqrt(max)



    while (next_prime < stop_at):
        for i in range(next_prime*2, max, next_prime):
            is_composite[i] = True
            next_prime += 2
        while (next_prime <= max and is_composite[next_prime]):
            next_prime += 2

    primes = []

    for i in range(2, max):
        if (not is_composite[i]):
                primes.append(i)

    return primes



num = 10
ans = findprimes(num)
print(ans)

