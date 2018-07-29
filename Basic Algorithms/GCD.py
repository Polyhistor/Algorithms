# Find the great common divisor of a and b
# GCD (a, b) = GDC (b, a MOD b).

# Integer: GCD(Integer:a, Integer: b)

#     while (b != 0)

#       // calculate the remainder
#       Integer: remainder = a mod b

#       //calculate GCD (b, remainder)
#       a = b
#       b = remainder

#       end while

# return a
# end GCD


def gcd (a,b):

    while(b):     # O(N)
      remainder = a % b # O(1)
      a, b = b, remainder; # O(1)

    return a

#Total : O(N)

print( gcd(5,10))


