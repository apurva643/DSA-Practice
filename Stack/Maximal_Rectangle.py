# LeetCode 85 - Maximal Rectangle
# Pattern: Monotonic Stack
# TC : O(rows × cols) | SC : O(cols)

def maximalRectangle(matrix):

    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    heights = [0] * cols
    max_area = 0

    for row in range(rows):

        # Build histogram heights for this row
        for col in range(cols):

            if matrix[row][col] == "1":
                heights[col] += 1
            else:
                heights[col] = 0

        # Find largest rectangle in the histogram
        stack = []
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

        heights.pop()

    return max_area
