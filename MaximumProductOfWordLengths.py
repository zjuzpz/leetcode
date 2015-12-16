"""
318. Maximum Product of Word Lengths
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""
# O(n ^ 2)
# O(n)
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lookup, res = [{} for i in range(len(words))], 0
        for i in range(len(words)):
            for w in words[i]:
                lookup[i][w] = True
            for j in range(0, i):
                for w in lookup[i]:
                    if w in lookup[j]:
                        break
                else:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

if __name__ == "__main__":
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    print(Solution().maxProduct(words))
