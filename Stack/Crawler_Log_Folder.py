# LeetCode 1598 - Crawler Log Folder
# Pattern: Stack (Basic Stack Operations)
# TC : O(n) | SC: O(n)

def minOperations(logs):

    stack = []
    for log in logs:

        if log == "./":
            continue

        elif log == "../":

            if stack:
                stack.pop()

        else:
            stack.append(log)

    return len(stack)

