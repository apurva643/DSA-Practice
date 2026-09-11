# LeetCode 739 - Daily Temperatures
# Pattern: Monotonic Stack (Next Greater Element)
# TC : O(n) | SC : O(n)


def dailyTemperatures(temperatures):

    stack = []  # stores indices
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):

        while stack and temperatures[i] > temperatures[stack[-1]]:

            previous_index = stack.pop()

            result[previous_index] = i - previous_index

        stack.append(i)

    return result
