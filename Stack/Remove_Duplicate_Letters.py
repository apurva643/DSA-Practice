# LeetCode 316 - Remove Duplicate Letters
# Pattern: Monotonic Stack
# TC : O(n) | SC : O(n)

def removeDuplicateLetters(s):

    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    stack = []
    seen = set()

    for ch in s:

        # One occurrence of ch is now being processed
        count[ch] -= 1

        if ch in seen:
            continue

        # Remove larger characters if they appear again later
        while stack and stack[-1] > ch and count[stack[-1]] > 0:

            removed = stack.pop()
            seen.remove(removed)

        stack.append(ch)
        seen.add(ch)

    return "".join(stack)
