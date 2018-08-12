# Find the largest number in an array

# Integer: FindLargest (Integer: array [])
#     Integer: largest = array [0]
#     For i = 1 to <largest index>
#           if (array[i] > largest)
#           then largest = array[i]
#     next i
#     return largest
# End FindLargest

def FL(arr,n):

    max = arr[0]

    for i in range(1,n):    #O(N)
        if (arr[i] > max):  #O(1)
            max = arr[i]    #O(1)

    return max

#Total O(N)

arr = [1,2,3]
n = len(arr)
ans = n
print (n)


