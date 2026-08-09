class Solution:
    def romanToInt(self, user):

        if user=="":
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

            if user[r] not in RTI:
                return 0
            else:
                if RTI[user[r+1]]>RTI[user[r]]:
                    output += (-RTI[user[r]])
                else:
                    output += (RTI[user[r]])
            r-=1

        return output