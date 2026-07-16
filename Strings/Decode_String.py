# LeetCode #394 - Decode String
# TC: O(n) | SC: O(n)

def decodeString(s):

    stack = []

    current_string = ""
    current_number = 0

    for ch in s:

        # If digit, build the complete number
        if ch.isdigit():
            current_number = current_number * 10 + int(ch)

        # Opening bracket
        elif ch == '[':
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0

        # Closing bracket
        elif ch == ']':
            previous_string, repeat = stack.pop()
            current_string = previous_string + current_string * repeat

        # Alphabet
        else:
            current_string += ch

    return current_string
