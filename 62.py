"""
62. 不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？



例如，上图是一个7 x 3 的网格。有多少可能的路径？

 

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
def uniquePaths(m: int, n: int):
    #空间复杂度O（m*n），时间复杂度O（m*n） 
    # pathList = [[0 for i in range(m)] for j in range(n)]
    # for i in range(m):
        # for j in range(n):
            # if (i*j) == 0:
                # pathList[j][i] = 1
            # else:
                # pathList[j][i] = pathList[j-1][i] + pathList[j][i-1]
    # return pathList[-1][-1]
    
    #空间复杂度O（2n）
    pre = [1] * m
    cur = [1] * m
    for i in range (1, n):
        for j in range(1, m):
            cur[j] = cur[j-1] + pre[j]
        pre = cur[ : ]
    return cur[-1]


m = 7
n = 3
print (uniquePaths(m, n))