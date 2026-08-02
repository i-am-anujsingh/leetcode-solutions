class Solution:
    def isPalindrome(self, x):
        
        if x<0:
            return False

        rev=0
        c=x
        while c>0:
            rev = (rev*10) + (c%10)
            c=c//10
        if x==rev :
            return True
        else:
            return False