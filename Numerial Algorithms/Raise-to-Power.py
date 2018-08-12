# Function to raise a number to power

# // Calculate A to the power p
# Float: RaiseTopower (Float: A, Integer: P)
#   <use A^2 x M = (A^M)^2 to quickly calculate A, A^2, A^4, A^6, A^8, and so on until you get to a value A^n where N + 1 > p>
#   <use those powers of A and A^M+N = A^M x A^N to calculate A^p>
#   Return A^P
# END RaiseToPower

import numpy as np

def RaisetoPower(a,p):
    print(a , p)
    if ( p==0 ):
        return 1

    elif ( p == 1 ):
        return a

    elif ( p % 2 == 0 ):
        a = RaisetoPower(a,p/2)          # O(log (p))
        return a * a

    else:
        return a * RaisetoPower(a,p-1)



print(RaisetoPower(2,9))

        