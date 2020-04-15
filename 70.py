# 动态规划，斐波那契数列
def climbStairs(n: int) -> int:
    dp1 = 1
    dp2 = 1
    if n <=1:
        return n
    for i in range(2, n+1):
        dp2 , dp1 = dp2+dp1, dp2
    return dp2


print (climbStairs(11))   