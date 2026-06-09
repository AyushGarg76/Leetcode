class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        unique = 1
        j = 1
        while (j < len(nums)):
            if nums[j] != nums[j-1]:
                i += 1
                nums[i] = nums[j]
                unique += 1
            j += 1
        return unique