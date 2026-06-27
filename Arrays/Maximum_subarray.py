# LeetCode #53: Maximum Subarray
# TC: O(n), SC: O(1)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum