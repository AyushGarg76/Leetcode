class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def square_add(n):
            sum1 = 0
            while n!=0:
                d = n % 10
                sum1 = sum1 + d*d
                n = n//10
            return sum1
        slow = n
        fast = n
        while True:
            slow = square_add(slow)
            fast = square_add(square_add(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False