"""
263. Ugly Number
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""
# O(logn)
# O(1)
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num >= 1:
            if num == 1:
                return True
            if num % 2 == 0:
                num = num / 2
                continue
            if num % 3 == 0:
                num = num / 3
                continue
            if num % 5 == 0:
                num = num / 5
                continue
            return False

if __name__ == "__main__":
    print(Solution().isUgly(14))
