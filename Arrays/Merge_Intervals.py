# LeetCode #56 - Merge Intervals
# Difficulty: Medium
# Pattern: Sorting + Interval Merging
# Time Complexity: O(n log n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort intervals based on the starting time
        intervals.sort()

        # Store the merged intervals
        result = []

        # Add the first interval
        result.append(intervals[0])

        # Traverse the remaining intervals
        for current in intervals[1:]:

            # Last interval in the result
            previous = result[-1]

            # Check if intervals overlap
            if current[0] <= previous[1]:

                # Merge by updating the ending point
                previous[1] = max(previous[1], current[1])

            else:
                # No overlap, add the current interval
                result.append(current)

        return result