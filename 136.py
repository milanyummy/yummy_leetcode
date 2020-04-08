def singleNumber(nums) -> int:
    #哈希表解法
    # dict1 = {}
    # for num in nums:
        # if num in dict1:
            # if dict1[num] == 1:
                # del dict1[num]
        # else:
            # dict1[num] = 1
    # return list(dict1.keys())[0]

    # 官方哈希表解法
    # dict1 = {}
    # for num in nums:
    #     try:
    #         dict1.pop(num)
    #     except:
    #         dict1[num] = 1
    # return dict1.popitem()[0] #popitem() 弹出字典最后一对键值，返回值为元祖

    #官方异或解法
    a = 0
    for i in nums:
        a ^= i
    return a

nums = [4,1,2,1,2]
print (singleNumber(nums))