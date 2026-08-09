class Solution:
    def romanToInt(self, user):
        if user=="":
            print("input can not be null")
            return 0
        user = user.upper()
        r = len(user)-1
        RTI = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,  "M":1000}
        if user[r] in RTI:
            output = RTI[user[r]]
        else:
            return 0
        r-=1
        while(r>=0):
            cur = user[r]
            pre = user[r+1]
            if cur not in RTI or pre not in RTI:
                    return 0
            else:
                if RTI[pre]>RTI[cur]:
                    output += (-RTI[cur])
                else:
                    output += (RTI[cur])
            r-=1
        return output