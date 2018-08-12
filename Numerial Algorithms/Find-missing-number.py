def getMissingNo(A):
    n = len(A)
    print(n)
    total = (n + 1) * (n + 2) / 2
    print(total)
    sum_of_A = sum(A)
    print (sum_of_A)
    return total - sum_of_A


# Driver program to test above function
A = [1, 2, 3, 4, 5, 6, 8, 9]
miss = getMissingNo(A)
print(miss)
