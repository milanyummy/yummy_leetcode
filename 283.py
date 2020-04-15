def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    k = 0
    for i in range(len(nums)):
        if nums[i-k] == 0:
            nums.append( nums.pop(i-k) )
            k += 1
        i += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)