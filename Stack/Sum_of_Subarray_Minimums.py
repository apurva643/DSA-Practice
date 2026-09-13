# LeetCode 907 - Sum of Subarray Minimums
# Pattern: Monotonic Stack
# TC : O(n) | SC : O(n)

def sumSubarrayMins(arr):

    MOD = 10**9 + 7
    stack = []
    result = 0

    for i in range(len(arr) + 1):

        current = arr[i] if i < len(arr) else 0

        while stack and (i == len(arr) or arr[stack[-1]] > current):

            mid = stack.pop()

            left = stack[-1] if stack else -1
            right = i

            left_count = mid - left
            right_count = right - mid

            result += arr[mid] * left_count * right_count

        stack.append(i)

    return result % MOD
