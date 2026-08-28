class Solution:
    def reverse(self, x):
        try:
            if x == 0:
                return 0
            sign = x//abs(x)
            st = str(abs(x))
            rev = int(st[::-1])*sign
            if (rev > 2**31 -1) or (rev < -2**31):
                return 0
            return rev
        except Exception as exp:
            return -1
        