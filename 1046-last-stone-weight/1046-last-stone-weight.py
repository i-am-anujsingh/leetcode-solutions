class Solution:
    def lastStoneWeight(self, stones):
        while(len(stones)!=1):
            a = max(stones)
            stones.pop(stones.index(a))
            b = max(stones)
            stones.pop(stones.index(b))
            w = max(a,b) - min(a,b)
            if w!=0:
                stones.append(w)
            if(not stones):
                return 0
        return stones[0]