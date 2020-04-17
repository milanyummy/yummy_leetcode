"""
55. 跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false

解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
def canJump(nums):
    #递归法，超时-_-#，问题可简化考虑
    #n = len(nums)
    #if nums[0] >= n-1:
    #    return True
    #for i in range (1, n):
    #    if nums[n-1-i] >= i:
    #        return canJump(nums[0:n-i])
    #    else:
    #        continue
    #return False

    #若全不为零，必可到达；若有0则判断该0可否跳过
    # n = len (nums)
    # for i in range(n-1):
        # if nums[i] != 0:
            # continue
        # else:
            # canPass0 = False
            # for j in range(1, i+1):
                # if nums[i-j]>j:
                    # canPass0 = True
                    # break
                # else:
                    # continue
            # if canPass0 is False:
                # return False
    # return True

    #官方解法：贪心算法，遍历数组维护可到达的最远位置farthest
    farthest = 0
    n = len(nums)
    for i in range(n):
        if i <= farthest:
            farthest = max(farthest, i+nums[i] )
            if farthest >= n-1:
                return True
    return False
                


nums = [0]
print( canJump(nums) )
