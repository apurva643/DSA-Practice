# LeetCode 84 - Largest Rectangle in Histogram
# Pattern: Monotonic Stack
# TC : O(n) | SC : O(n)

def largestRectangleArea(heights):

    stack = []
    max_area = 0

    heights.append(0)

    for i in range(len(heights)):

        while stack and heights[i] < heights[stack[-1]]:

            height = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            area = height * width

            max_area = max(max_area, area)

        stack.append(i)

    return max_area
