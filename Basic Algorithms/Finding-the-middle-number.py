# Finding the number in middle of an array (this will serve as a part of a greater alogrithm, so you may night find it useful alone)

# Integer: Dividingpoint (Integer: array[])
#    Integer: number1 = array[0]
#    Integer: number2 = array[<last index of array>]
#    Integer: number2 = array[<last index of array> / 2]

#    If (<number1 is between number2 and number3>) return number 1
#    If (<number2 is between number1 and number3>) return number 2
#    Return number3

# End Middlevalue



def DP (arr):

    num1 = arr[0]
    num2 = arr[-1]
    num3 = arr[-1]/2

    if (num2 <= num1 <= num3):              # O(1)
        if (num1 <= num2 <= num3):          # O(1)
            return num3
        else:
            return num2
    return num1

# Total = O(1)

arr = [1,2,3,4,5]
ans = DP(arr)
print(ans)

