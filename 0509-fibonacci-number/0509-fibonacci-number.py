class Solution:
    def fib(self, n):
        a = 0
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return b
            
        for i in range(1, n):
            f = a+b
            a, b = b, f
        return b        