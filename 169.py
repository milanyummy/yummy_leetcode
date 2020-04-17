"""
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def majorityElement(nums):
    # 哈希表，比较蠢的应用方法
    #dic = {}
    #n = len(nums)
    #if n == 1:
    #    return nums[0]
    #for num in nums:
    #    if dic.get(num):
    #        dic[num] += 1
    #        if dic[num] >= n/2:
    #            return num
    #    else:
    #        dic[num] = 1

    #Boyer-Moore 投票算法
    count = 0
    for num in nums:
        if count == 0:
            most = num
            count += 1
        elif most == num:
            count += 1
        else:
            count -= 1
    return most
        


nums = [3,2,3]

print(majorityElement(nums))