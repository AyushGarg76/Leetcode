class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)

        max_end = max_sum = nums[0]
        min_end = min_sum = nums[0]

        for i in range(1, len(nums)):

            max_end = max(nums[i], max_end + nums[i])
            max_sum = max(max_sum, max_end)

            min_end = min(nums[i], min_end + nums[i])
            min_sum = min(min_sum, min_end)
        
        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)