"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [flowerbed[0]] + flowerbed + [flowerbed[-1]]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True)
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False)
    print(solution.canPlaceFlowers([0, 0, 1, 0, 1], 1) == True)
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2) == True)
    print(solution.canPlaceFlowers([1, 0], 1) == False)
