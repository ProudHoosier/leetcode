class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        
        for i in range(0,l):
            for j in range(0,l):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]