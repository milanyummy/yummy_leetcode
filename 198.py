def rob(nums):
    #自写动态规划、递归 超时
    # dp1 = dp2 = 0
    # def dp(n, nums):
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return nums[0]
    #     if n == 2:
    #         dp1 = nums[0]
    #         return max(nums[0], nums[1])
    #     else:
    #         dp1 = dp(n-1, nums)
    #         dp2 = dp(n-2, nums)
    #         return max(dp1, dp2+nums[n-1])
    # return dp(len(nums), nums)
    
    #动态规划、递推解法
    n = len(nums)

    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp1 = nums[0]
    dp2 = 0
    ans = 0
    for i in range(2, n+1):
        ans = max(dp2+nums[i-1], dp1)
        dp2 = dp1
        dp1 = ans
    return ans

nums =  [2,7,9,3,1]
print( rob(nums) )