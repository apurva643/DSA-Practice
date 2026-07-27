# LeetCode 1021 - Remove Outermost Parentheses
# Pattern: Stack (Basic Stack Operations)
# TC : O(n) | SC: O(n)

def removeOuterParentheses(s):

    stack = []
    answer = ""

    for ch in s:

        if ch == "(":

            if stack:
                answer += ch

            stack.append(ch)

        else:

            stack.pop()

            if stack:
                answer += ch

    return answer

