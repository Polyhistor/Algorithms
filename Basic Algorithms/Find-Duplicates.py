#Find duplicates in arrays

#Boolean: Containsduplicate(Integer: array[])
#    // loop over all of the array's items
#    for i = 0 to <largest index>
#        for j = 0 to <largest index>
#        // see if these two items are duplicates
#        if ( i =! j ) then
#            if ( array[i] == array[j] ) then return true
#        end if
#     next j


def FD(arr,n):

    checker = False

    for i in range(0, n):                   #O(N)
        for j in range(0,n):                #O(N)
            if (i != j ):                   #O(1)
                if (arr[i] == arr[j]):
                    checker = True

    return checker

#Total = O( N x N ) = O( N^2)

arr = [1,2,2,4]
n = len(arr)
ans = FD(arr,n)
print (ans)