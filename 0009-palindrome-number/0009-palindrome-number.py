class Solution:
    def isPalindrome(self, x):

        st = str(x)
        rev = st[::-1]
        print(st, rev)

        if (st == rev):
            return True
        else:
            return False