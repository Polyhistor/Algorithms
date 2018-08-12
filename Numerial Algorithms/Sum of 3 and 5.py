def stn(arr):

    n = len(arr)
    array2 = []
    sum = 0

    for i in range(0, n):
        print (i)
        if (arr[i] % 5 == 0 or arr[i] % 3 == 0):
            print (arr[i])
            sum += arr[i]


    return sum


anotherarr = list(range(1000))
ans = stn(anotherarr)
string = "the sum is"
print (string, ans)