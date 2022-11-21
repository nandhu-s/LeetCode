class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        p1, p2 = 0, 1
        for i in range(1,n):
            p1, p2 = p2, p1 + p2           
        return p2
