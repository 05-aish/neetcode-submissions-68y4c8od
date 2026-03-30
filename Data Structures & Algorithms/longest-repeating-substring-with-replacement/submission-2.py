class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        maxLen = 0
        fmap = {}
        while(r < n):

            fmap[s[r]] = fmap.get(s[r], 0) + 1
            print(f"r={r} s[r]={s[r]} l={l} fmap={fmap} replacements={(r-l)-max(fmap.values())}")
    
            
            while((r - l + 1) - max(fmap.values()) > k):
                fmap[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen