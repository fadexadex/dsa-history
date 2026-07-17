# Day notes: cooking

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        res = 0
        if n == 1:
            return 1
        for _ in range(n - 1):
            res = one + two
            two = one
            one = res
        return res
