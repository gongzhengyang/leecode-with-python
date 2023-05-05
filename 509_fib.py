class Solution:
    def fib(self, n: int) -> int:
        solved = {0: 0, 1: 1}

        def sub_fib(value):
            if value not in solved:
                solved[value] = sub_fib(value - 1) + sub_fib(value - 2)
            return solved[value]

        return sub_fib(n)
