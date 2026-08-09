class Solution:
    def romanToInt(self, user):
        if user=="":
            print("input can not be null")
            return 0
        user = " ".join(user).upper().split(" ")
        r = len(user)-1
        RTI = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,  "M":1000}
        if user[r] in RTI.keys():
            int = RTI[user[r]]
        else:
            return 0
        r-=1
        flag = False
        while(r>=0):
            cur = user[r]
            pre = user[r+1]   
            if pre != cur:
                if cur not in RTI.keys() or pre not in RTI.keys():
                    return 0
                if RTI[pre]>RTI[cur]:
                    int = int + (-RTI[cur])
                else:
                    int = int + (RTI[cur])
            else:
                if cur not in RTI.keys() or pre not in RTI.keys():
                    return 0
                int = int + (RTI[cur])
            r-=1
        return int