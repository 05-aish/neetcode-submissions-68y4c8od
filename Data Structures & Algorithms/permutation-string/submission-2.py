class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = 0
        n = len(s2)
        windowLen = len(s1)

        if n < windowLen: return False

        #s1 map and window of s2 map
        fmap = {}
        fmapCurr = {}

        #frequency map for s1
        while(x < windowLen):
            fmap[s1[x]] = fmap.get(s1[x], 0) + 1
            x += 1

        #frequency map for intial window of size s1 in s2
        for i in range(windowLen):
            fmapCurr[s2[i]] = fmapCurr.get(s2[i], 0) + 1
        if fmapCurr == fmap:
            return True
        
        #fixed size window 0 to len(s1)
        r = windowLen
        l = 0
        while(r < n):
            
            fmapCurr[s2[l]] -= 1
            if fmapCurr[s2[l]] == 0:
                del fmapCurr[s2[l]]
            l += 1

            fmapCurr[s2[r]] = fmapCurr.get(s2[r], 0) + 1
            r += 1

            if fmapCurr == fmap:
                return True
                
        return False
        