# Checking out if one array is the rotation of the other

def checkrotate(a,b):

    n = len(a)
    no = len(b)
    true = 0

    for i in range(n):
        for j in range(no):
            if (a[i] == b[j]):
                true += 1



    if true == len(a):
        return "Fucking rotation!"
    else:
        return "Not a fucking rotation x)"



lsd = [1,2,3,4,5]
lsdd = [5,4,3,2,6]

ans = checkrotate(lsd,lsdd)
print(ans)