# LeetCode #31 - Next Permutation
# Difficulty: Medium
# Pattern: Array
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        n = len(nums)

        pivot = -1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot != -1:

            for i in range(n - 1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break

        left = pivot + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


