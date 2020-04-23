"""
面试题 08.11. 硬币
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

示例1:

 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:

 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
说明：

注意:

你可以假设：

0 <= n (总金额) <= 1000000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
def waysToChange(n: int) -> int:
    if n == 0:
        return 0
    waysList = [1]*(n+1)
    for i in range(n+1):
        if i < 5:
            waysList[i] = waysList[i-1]
        elif i < 10:
            waysList[i] = waysList[i-1] + waysList[i-5]
        elif i < 25:
            waysList[i] = waysList[i-1] + waysList[i-5] + waysList[i-10]
        else:
            waysList[i] = waysList[i-1] + waysList[i-5] + waysList[i-10] + waysList[i-25]
    return waysList[-1]

print(waysToChange(6))