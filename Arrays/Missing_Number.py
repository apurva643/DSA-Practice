# LeetCode #268 - Missing Number
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected_sum = n * (n + 1) // 2

        actual_sum = sum(nums)

        return expected_sum - actual_sum