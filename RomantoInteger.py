"""
13. Roman to Integer
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""
# O(n)
# O(1)
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and lookup[s[i]] < lookup[s[i + 1]]:
                res -= lookup[s[i]]
            else:
                res += lookup[s[i]]
        return res

if __name__ == "__main__":
    print (Solution().romanToInt("MMMCMXCIX"))
