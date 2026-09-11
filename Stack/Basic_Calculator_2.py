# LeetCode 227 - Basic Calculator II
# TC : O(n) | SC : O(n)

def calculate(s):

    stack = []
    num = 0
    sign = "+"

    for i in range(len(s)):

        ch = s[i]
        
        if ch.isdigit():
            num = num * 10 + int(ch)

        if (not ch.isdigit() and ch != " ") or i == len(s) - 1:

            if sign == "+":
                stack.append(num)

            elif sign == "-":
                stack.append(-num)

            elif sign == "*":
                stack.append(stack.pop() * num)

            elif sign == "/":
                stack.append(int(stack.pop() / num))

            sign = ch
            num = 0

    return sum(stack)
