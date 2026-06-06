class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_nums = sorted(nums)
        for k in range(len(nums)):
            a = nums[-k:] + nums[:-k]
            if a == sorted_nums:
                return True
        return False
        