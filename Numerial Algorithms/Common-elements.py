#Finding the common elements

def findcommon(a,b):

    common =[]
    n = len(a)
    n2 = len(b)

    for i in range(n):
        for j in range(n2):
            if a[i] == b[j]:
                common.append(a[i])

    return {
        "the common elements are:" : common
    }


lsd = [1,2,3,4,5,6]
lsdtwo = [1,3,4,5,7,8,9]

ans = findcommon(lsd,lsdtwo)
print(ans)