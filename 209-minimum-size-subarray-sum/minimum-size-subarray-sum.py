class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        high = 0
        low = 0
        result = float('inf')
        n = len(nums)
        sum1 = 0
        while(high<n):
            sum1 = sum1 + nums[high]
            while(sum1 >= target):
                length = high - low + 1
                result = min(result, length)
                sum1 = sum1 - nums[low]
                low += 1
            high += 1
        return 0 if result == float('inf') else result