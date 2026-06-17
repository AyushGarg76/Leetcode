class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero = 0
        one = 0

        freq = {}

        result = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                zero += 1
            else:
                one += 1

            diff = zero - one

            if diff == 0:
                result = max(result, i + 1)

            if diff not in freq:
                freq[diff] = i

            else:
                idx = freq[diff]

                length = i - idx

                result = max(result, length)

        return result