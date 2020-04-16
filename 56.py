"""
56. 合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

#先按照各区间左端点排序，然后依次判断相邻区间能否合并
def merge(intervals):
    list1 = sorted(intervals, key=lambda s: s[0])
    length = len(list1)
    i = 0
    while i < length-1:
        if list1[i][1] < list1[i+1][0]:
            i += 1
        else:
            list1[i] = [min(list1[i][0], list1[i+1][0]), max(list1[i][1], list1[i+1][1])]
            del list1[i+1]
            length -=1
    return list1
intervals = [[1,4],[4,5]]
print (merge(intervals))