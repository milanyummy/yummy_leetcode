def search(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        return -1
nums = [4,5,6,7,0,1,2]
target = 3
print (search(nums, 0))