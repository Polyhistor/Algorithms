# Rotating a 2d array by 90 degree

def array_rotator(arr, n):

    new_arr = []

    for i in reversed(range(n)):
        for j in reversed(range(n)):
            new_arr.append(arr[j][i])

    return new_arr


arr = [[1,2,3],[4,5,6],[7,8,9]]
ans = array_rotator(arr,3)
ans2= [ans[x:x+3] for x in range(0,len(ans),3)]
ans2.reverse()
print(ans2)




