# Finding prime factors

# List of Integer: FindFactors(Integer: numer)
#
#   List of Integer: factors
#   Integer: i = 2
#
#   While ( i < number )
#
#        // pull out factors of i
#        While ( number Mod i == 0 )
#
#            // i is a factor. Add it to the list.
#            factors.Add(i)
#
#            // Divide the number by i .
#            number = number / i
#
#   End While

# If there's anything left of the number, it is a factor, too.
#
#   If ( number > 1 ) then factors.Add (number)
#        return factors
#
# END FindFactors

