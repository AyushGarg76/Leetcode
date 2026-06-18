class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])

        result = []

        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for i in range(1, len(intervals)):
            start2 = intervals[i][0]
            end2 = intervals[i][1]

            if start2 <= end1:          # overlap
                end1 = max(end1, end2)
            else:                       # no overlap
                result.append([start1, end1])

                start1 = start2
                end1 = end2

        result.append([start1, end1])

        return result