
def isPalindrome(x: int) -> bool:
    # 取余按位获取
    # if x < 0:
        # return False
    # elif x == 0:
        # return True
    # numList = []
    # while (x > 0):
        # numList.append(x % 10)
        # x //= 10
    # if numList == list(reversed(numList)):
        # return True
    # else:
        # return False
    
    #字符串解法
    numStr = str(x)
    if numStr[: :-1] == numStr:
        return True
    else:
        return False

x = 121
print(isPalindrome(x))