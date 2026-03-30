class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        maxLen = 0
        maxFreq = 0
        fmap = {}
        while(r < n):

            fmap[s[r]] = fmap.get(s[r], 0) + 1
            r += 1

            while((r - l) - max(fmap.values()) > k):
                fmap[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l)

        return maxLen