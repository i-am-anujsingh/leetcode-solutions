class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        s+=s[::-1]
        del s[:l]
        