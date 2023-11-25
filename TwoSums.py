class Solution(object):
    def twoSum(self, nums, target):
        x={}
        for i, num in enumerate(nums):
            if target - num in x:
                return [x[target - num], i]
            x[num] = i