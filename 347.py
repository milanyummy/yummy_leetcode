"""
347. 前 K 个高频元素

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
import heapq
def topKFrequent(nums, k: int):
    #哈希表取前n个值
    #dic = {}
    #ans = []
    #for num in nums:
    #    if dic.get(num):
    #        dic[num] += 1
    #    else:
    #        dic[num] = 1
    #for i in range (k):
    #    this = max(dic, key=dic.get)
    #    ans.append(this)
    #    del dic[this]
    #return ans

    #python 流氓解法
    count = collections.Counter(nums)        
    return heapq.nlargest(k, count.keys(), key=count.get)

nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))