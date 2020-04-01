# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:50:35 2020

@author: YummY
"""

import copy
nums = [3, 3]
target = 6
for item in nums:
    numsBak = copy.copy(nums)
    numsBak.remove(item)
    if (target-item) in nums:
        p1 = nums.index(item)
        p2 = nums.index(target-item) + 1
        break
print(p1,p2)