def multiply(arr):

    n = len(arr)
    sum = []


    for i in range(n):

        print(i)

        for j in range(n):

            print(j)

            if arr[i] * arr[j] == 20:
                sum.append(arr[i])

    return sum


arr = [1,2,3,4,5,10]
ans = multiply(arr)
print(ans)
