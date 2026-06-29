# LeetCode #169 - Majority Element
# Difficulty: Easy
# Pattern: Hash Map (Dictionary)
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num in count:
            if count[num] > len(nums) // 2:
                return num