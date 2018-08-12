# find duplicates in a list and store it in a dictionary

def finddupli(arr):

    dict={}

    for e in arr:
        dict[e] = dict.get(e,0)+1



    return dict



lsd = [1,2,3,4,5,2,5,]
ans = finddupli(lsd)
print(ans)

sorted = [key for key,value in ans.items() if value > 1]
print(sorted)