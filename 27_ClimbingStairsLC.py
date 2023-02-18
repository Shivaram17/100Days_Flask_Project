class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1 
        fib1 = 1
        fib2 = 2

        for i in range(3, n+1):
            next_fib = fib1 + fib2
            fib1 = fib2
            fib2 = next_fib
        return fib2
