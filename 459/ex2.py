"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.



Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                if s[:i] * (len(s) // i) == s:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.repeatedSubstringPattern("abab") == True)
    print(solution.repeatedSubstringPattern("aba") == False)
    print(solution.repeatedSubstringPattern("abcabcabcabc") == True)
    print(solution.repeatedSubstringPattern("ababab") == True)
    print(solution.repeatedSubstringPattern("bb") == True)
