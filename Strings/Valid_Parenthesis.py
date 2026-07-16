# LeetCode #20 - Valid Parentheses
# TC : O(n) | SC : O(n)

def isValid(s):

    stack = []

    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:

        if ch in mapping:

            if not stack or stack[-1] != mapping[ch]:
                return False

            stack.pop()

        else:
            stack.append(ch)

    return len(stack) == 0
