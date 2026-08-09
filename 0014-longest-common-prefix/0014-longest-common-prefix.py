class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        indx = 0
        try:
            while True:
                for i in range(1,len(strs)):
                    if strs[0][indx] != strs[i][indx]:
                        return prefix
                prefix += strs[0][indx]
                indx += 1
                if indx>=len(strs[0]):
                    return prefix
        except Exception as exp:
            return prefix