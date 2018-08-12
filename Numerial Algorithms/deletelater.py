
def mostoccuring(str):

    dict = {}

    for char in str:
        dict[char] = dict.get(char,0) +1


    biggest = [None,0]
    second = [None, 0]

    for e in dict.items():
        char, count = e
        if(count > biggest[1]):
            second,biggest = biggest,e

        elif(count > second[1]):
            second = e


    return{
        "the biggest element is :" : biggest[0],
        "the second biggest element is :" : second[0]
    }


str= "aaabbbbcccddddd"
ans = mostoccuring(str)
print(ans)