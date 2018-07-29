# Find the great common divisor of a and b
# GCD (a, b) = GDC (b, a MOD b).


def computeGCD(x, y):
    while (y):
        x, y = y, x % y

    return x


a = 60
b = 48


print("The gcd of 60 and 48 is : ", end="")
print(computeGCD(60, 48))