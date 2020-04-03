def sortArray(nums):
    #冒泡排序：两两比较，将大的元素向后交换
    # flag = True
    # while flag is True:
        # flag = False
        # for i in range (len(nums)-1):
            # if nums[i] > nums[i+1]:
                # nums[i], nums[i+1] = nums[i+1], nums[i]
                # flag = True
    # return nums

    #选择排序：每一趟选择剩余元素中最小的
    # for i in range(len(nums) - 1):
    #     min = i
    #     for j in range(i+1, len(nums)):
    #         if nums[i] > nums[j]:
    #             min = j
    #     if min != i:
    #         nums[i], nums[min] = nums[min], nums[i]
    # return nums

    #插入排序：将每个元素插入到已排序好的序列中
    # for i in range (len(nums)):
    #     for j in range(i):
    #         if nums[i] < nums[j]:
    #             nums.insert(j, nums.pop(i))
    # return nums

    #二分插入排序：在序列有序部分中通过二分法找到新元素的位置gcgnxz
    # for i in range (1, len(nums)):
    #     low = 0
    #     high = i-1
    #     
    #     while low <= high:
    #         m = int((low+high) / 2)
    #         if nums[i] < nums[m]:
    #             high = m -1
    #         else:
    #             low = m + 1
    #     nums.insert(low , nums.pop(i))#low == high +1
    # return nums 
    
    #快速排序：选取一个基准值，小数在左大数在右，然后分区递归进行
    def quickSort(qlist, start, end):
        if start >= end:
            return
        pivot = qlist[start]
        low = start
        high = end
        while low < high:
            while low < high and qlist[high] >= pivot:
                high -= 1
            qlist[low] = qlist[high]
            while low < high and qlist[low] < pivot:
                low += 1
            qlist[high] = qlist[low]
        qlist[low] = pivot
        quickSort(qlist, start, low-1)
        quickSort(qlist, low+1, end) 
    
    quickSort(nums, 0, len(nums)-1)
    return nums

nums = [5,1,1,2,0,0]

print(sortArray(nums))