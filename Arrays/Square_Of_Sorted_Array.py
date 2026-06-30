# LeetCode #977 - Squares of a Sorted Array
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = [0] * n

        left = 0
        right = n - 1

        position = n - 1

        while left <= right:

            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                answer[position] = left_square
                left += 1
            else:
                answer[position] = right_square
                right -= 1

            position -= 1

        return answer
