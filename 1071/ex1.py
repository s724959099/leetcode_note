"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        length = min(len(str1), len(str2))
        for i in range(length, 0, -1):
            if len(str1) % i != 0 or len(str2) % i != 0:
                continue

            if str1[:i] != str2[:i]:
                continue
            ret = str1[:i]
            if str1 == ret * (len(str1) // i) and str2 == ret * (len(str2) // i):
                return ret
        return ""


if __name__ == '__main__':
    solution = Solution()
    print(solution.gcdOfStrings("ABCABC", "ABC") == "ABC")
    print(solution.gcdOfStrings("ABABAB", "ABAB") == "AB")
    print(solution.gcdOfStrings("LEET", "CODE") == "")
