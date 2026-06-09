class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        b = []

        for x in nums:
            if x < 0:
                a.append(x * x)
            else:
                b.append(x * x)

        a.reverse()

        result = []
        i = j = 0

        while(i < len(a) and j < len(b)):
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        while(j < len(b)):
            result.append(b[j])
            j += 1
        while(i < len(a)):
            result.append(a[i])
            i += 1
        return result
