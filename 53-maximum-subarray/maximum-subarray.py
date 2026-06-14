class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_ending = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            best_ending = max(nums[i], best_ending + nums[i])
            ans = max(ans, best_ending)
        return ans