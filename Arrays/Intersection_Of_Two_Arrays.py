# LeetCode #349 - Intersection of Two Arrays
# Time Complexity: O(n + m)
# Space Complexity: O(n)

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        seen = set(nums1)

        result = set()

        for num in nums2:
            if num in seen:
                result.add(num)

        return list(result)