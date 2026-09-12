# LeetCode 901 - Online Stock Span
# Pattern: Monotonic Stack
# TC : O(n) overall | SC : O(n)

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):

        span = 1

        while self.stack and self.stack[-1][0] <= price:

            previous_price, previous_span = self.stack.pop()

            span += previous_span

        self.stack.append((price, span))

        return span

