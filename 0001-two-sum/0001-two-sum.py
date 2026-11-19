class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
             remainings=target-nums[i]
             if remainings in nums and nums.index(remainings)!=i:
               return[i,nums.index(remainings)]