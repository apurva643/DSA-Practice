# LeetCode #26: Remove Duplicates from Sorted Array
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Handle empty array
        if len(nums) == 0:
            return 0

        # i points to the last unique element
        i = 0

        # j scans the array
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        # Number of unique elements
        return i + 1