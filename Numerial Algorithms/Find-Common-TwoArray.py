# finding the common elements in two arrays


def findcommon(a,b):

    lst = []

    n = len(a)
    no = len(b)

    for i in range(n):
        for j in range(no):
            if a[i] == b[j]:
                lst.append(a[i])


    return set(lst)



lsd = [6,7,8]
lsdd = [1,2,3,4,5,4,8]

ans = findcommon(lsd,lsdd)
print(ans)